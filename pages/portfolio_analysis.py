import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from io import BytesIO
from fpdf import FPDF
# --- Stock Data Functions ---

def fetch_stock_data(tickers, start_date, end_date):
    try:
        stock_data = yf.download(tickers, start=start_date, end=end_date)['Close']
        if isinstance(stock_data, pd.Series):
            stock_data = stock_data.to_frame()
        stock_data.dropna(axis=1, how="all", inplace=True)
        
        if stock_data.empty:
            raise ValueError("No valid stock data found for the given tickers and date range.")
        return stock_data
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return pd.DataFrame() 

def fetch_benchmark_data(start_date, end_date):
    try:
        benchmark_ticker = "^GSPC"  
        benchmark_data = yf.download(benchmark_ticker, start=start_date, end=end_date)['Close']

        if benchmark_data.empty:
            raise ValueError("No benchmark data found for the given date range.")
        return benchmark_data
    except Exception as e:
        print(f"Error fetching benchmark data: {e}")
        return pd.Series() 

# --- Portfolio Value Calculations ---
def calculate_portfolio_value(stock_data, allocations, initial_investment):
    normalized_prices = stock_data / stock_data.iloc[0]  
    portfolio_weights = pd.Series(allocations)
    portfolio_value = normalized_prices.dot(portfolio_weights) * initial_investment
    return portfolio_value

# --- Risk/Return Calculations ---
def calculate_beta(portfolio_returns, benchmark_returns):
    portfolio_returns = np.array(portfolio_returns).flatten()  
    benchmark_returns = np.array(benchmark_returns).flatten()  

    print(f"Portfolio Returns Shape: {portfolio_returns.shape}")
    print(f"Benchmark Returns Shape: {benchmark_returns.shape}")

    if portfolio_returns.shape != benchmark_returns.shape:
        raise ValueError("Mismatched data shapes. Check alignment before computing beta.")

    covariance = np.cov(portfolio_returns, benchmark_returns)[0, 1]
    benchmark_variance = np.var(benchmark_returns)
    beta = covariance / benchmark_variance
    return beta

def calculate_treynor_ratio(portfolio_return, risk_free_rate, beta):
    return (portfolio_return - risk_free_rate) / beta

def calculate_risk_return_metrics(portfolio_value, benchmark_data, risk_free_rate=0.02):
    daily_returns = portfolio_value.pct_change().dropna()
    benchmark_returns = benchmark_data.pct_change().dropna()

    # Align dates
    aligned_data = daily_returns.index.intersection(benchmark_returns.index)
    daily_returns = daily_returns.loc[aligned_data]
    benchmark_returns = benchmark_returns.loc[aligned_data]

    if len(daily_returns) == 0 or len(benchmark_returns) == 0:
        raise ValueError("Insufficient overlapping data between portfolio and benchmark.")

    annual_return = daily_returns.mean() * 252
    annual_volatility = daily_returns.std() * (252 ** 0.5)
    sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility

    beta = calculate_beta(daily_returns, benchmark_returns)
    treynor_ratio = calculate_treynor_ratio(annual_return, risk_free_rate, beta)

    return annual_return, annual_volatility, sharpe_ratio, beta, treynor_ratio


# --- Additional Metrics ---
def calculate_moving_average(stock_data, window=50):
    return stock_data.rolling(window=window).mean()

def calculate_rsi(stock_data, period=14):
    delta = stock_data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def create_buy_sell_signals(stock_data):
    # Moving Average strategy for buy/sell recommendation
    ma50 = calculate_moving_average(stock_data, window=50)
    ma200 = calculate_moving_average(stock_data, window=200)
    rsi = calculate_rsi(stock_data)

    # Generate buy/sell signals
    signals = pd.DataFrame(index=stock_data.index)
    signals['Signal'] = np.where(ma50 > ma200, 'Buy', 'Sell')
    signals['RSI'] = rsi
    signals['RSI Signal'] = np.where(rsi < 30, 'Buy', np.where(rsi > 70, 'Sell', 'Hold'))

    return signals, ma50, ma200, rsi

# --- Report Generation ---
def create_excel_report(portfolio_data, metrics):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        portfolio_data.to_excel(writer, sheet_name="Portfolio Data", index=False)
        metrics.to_excel(writer, sheet_name="Performance Metrics", index=False)
    
    output.seek(0)
    return output

def create_pdf_report(portfolio_data, metrics):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Portfolio Performance Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Portfolio Data:", ln=True)
    pdf.ln(5)

    for col in portfolio_data.columns:
        pdf.cell(40, 10, txt=col, border=1, align="C")
    pdf.ln()

    for i in range(len(portfolio_data)):
        for col in portfolio_data.columns:
            pdf.cell(40, 10, txt=str(portfolio_data[col].iloc[i]), border=1, align="C")
        pdf.ln()

    pdf.ln(10)
    pdf.cell(200, 10, txt="Performance Metrics:", ln=True)
    pdf.ln(5)

    for metric, value in metrics.items():
        pdf.cell(200, 10, txt=f"{metric}: {value}", ln=True)

    pdf_output = pdf.output(dest='S')  
    pdf_output = BytesIO(pdf_output.encode('latin1')) 
    pdf_output.seek(0) 
    return pdf_output

def comparison_indicator(portfolio_value, benchmark_value):
    if isinstance(portfolio_value, pd.Series):
        portfolio_value = portfolio_value.iloc[-1] 
    if isinstance(benchmark_value, pd.Series):
        benchmark_value = benchmark_value.iloc[-1]  

    return "📈" if portfolio_value > benchmark_value else "📉"

# --- Streamlit Interface ---
st.title("Portfolio Performance Tracker")

with st.expander("Portfolio Inputs"):
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Step 1: Select Stock Tickers")
        predefined_stocks = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA", "META", "NFLX", "NVDA", "BRK-B", "JPM"]
        tickers = st.multiselect(
            "Choose stocks to include in your portfolio:",
            options=predefined_stocks,
            default=["AAPL", "MSFT"]
        )

    with col2:
        st.write("### Step 2: Allocate Portfolio Weights")
        allocations = {}
        for ticker in tickers:
            weight_percentage = st.slider(
                f"Weight for {ticker} (%):",
                min_value=0.0,
                max_value=100.0,
                value=50.0 if ticker in ["AAPL", "MSFT"] else 0.0,
                step=1.0,
                key=ticker
            )
            allocations[ticker] = weight_percentage / 100
        if allocations and sum(allocations.values()) != 1.0:
            st.error("Portfolio weights must sum to 100%. Please adjust the weights.")
        if st.button("Reset weights"):
            for ticker in tickers:
                allocations[ticker] = 0
            allocations["AAPL"] = 0.5
            allocations["MSFT"] = 0.5

    col3, col4 = st.columns(2)

    with col3:
        start_date = st.date_input("Start Date", value=pd.Timestamp("2022-01-01"))

    with col4:
        end_date = st.date_input("End Date", value=pd.Timestamp("2023-01-01"))

    initial_investment = st.number_input("Initial Investment", value=100000, step=1000)

if st.button("Analyze Portfolio") and tickers and sum(allocations.values()) == 1.0:
    with st.spinner("Analyzing Portfolio..."):
        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = end_date.strftime('%Y-%m-%d')

        stock_data = fetch_stock_data(tickers, start_date_str, end_date_str)
        benchmark_data = fetch_benchmark_data(start_date_str, end_date_str)

        if stock_data.empty:
            st.error("No data found for the selected tickers and date range.")
        else:
            portfolio_value = calculate_portfolio_value(stock_data, allocations, initial_investment)
            annual_return, annual_volatility, sharpe_ratio, beta, treynor_ratio = calculate_risk_return_metrics(portfolio_value, benchmark_data)
            benchmark_return, benchmark_volatility, benchmark_sharpe, benchmark_beta, benchmark_treynor = calculate_risk_return_metrics(benchmark_data, benchmark_data)

            st.markdown("---")
            st.subheader("Portfolio Performance Metrics")
            col5, col6, col7, col8, col9 = st.columns(5)
        
            with col5:
                indicator_return = comparison_indicator(annual_return, benchmark_return)
                st.metric(label="Annual Return", value=f"{annual_return:.2%}", delta=indicator_return, delta_color="normal")
            
            with col6:
                indicator_volatility = comparison_indicator(annual_volatility, benchmark_volatility)
                st.metric(label="Annual Volatility", value=f"{annual_volatility:.2%}", delta=indicator_volatility, delta_color="normal")
            
            with col7:
                indicator_sharpe = comparison_indicator(sharpe_ratio, benchmark_sharpe)
                st.metric(label="Sharpe Ratio", value=f"{sharpe_ratio:.2f}", delta=indicator_sharpe, delta_color="normal")
            
            with col8:
                indicator_beta = comparison_indicator(beta, benchmark_beta)
                st.metric(label="Beta", value=f"{beta:.2f}", delta=indicator_beta, delta_color="normal")
            
            with col9:
                indicator_treynor = comparison_indicator(treynor_ratio, benchmark_treynor)
                st.metric(label="Treynor Ratio", value=f"{treynor_ratio:.2f}", delta=indicator_treynor, delta_color="normal")

            st.markdown("---")
            st.subheader("Portfolio vs. S&P 500 Performance")

            portfolio_value_normalized = portfolio_value / portfolio_value.iloc[0] * 100
            benchmark_data_normalized = benchmark_data / benchmark_data.iloc[0] * 100

            df_comparison = pd.DataFrame({
                "Portfolio": np.ravel(portfolio_value_normalized),
                "S&P 500": np.ravel(benchmark_data_normalized)
            })
            
            st.plotly_chart(px.line(df_comparison, title="Portfolio vs S&P 500 Performance"))

            st.markdown("---")
            st.subheader("Buy/Sell Recommendations")

            for ticker in tickers:
                st.write(f"### {ticker} - Buy/Sell Signals")
                stock = stock_data[ticker]
                signals, ma50, ma200, rsi = create_buy_sell_signals(stock)

                latest_signal = signals.tail(1)
                recommendation = latest_signal['Signal'].values[0]
                rsi_signal = latest_signal['RSI Signal'].values[0]

                signal_emoji = "✅" if recommendation == "Buy" else "❌"
                st.markdown(f"**Recommendation:** {signal_emoji} {recommendation}")
                
                st.write(f"**RSI Signal:** {rsi_signal}")
                
                st.plotly_chart(px.line(stock, title=f"{ticker} Stock Price")\
                    .add_scatter(x=ma50.index, y=ma50, mode="lines", name="50-day MA")\
                    .add_scatter(x=ma200.index, y=ma200, mode="lines", name="200-day MA"))

                st.plotly_chart(px.line(rsi, title=f"{ticker} RSI (Relative Strength Index)"))
            
            st.markdown("---")
            st.subheader("Download Reports")
            allocations_df = pd.DataFrame({
            "Stock": allocations.keys(),
            "Weight": allocations.values()
            })

            
            excel_report = create_excel_report(df_comparison, allocations_df)
            st.download_button(
                label="Download Excel Report",
                data=excel_report,
                file_name="portfolio_report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            
            pdf_report = create_pdf_report(df_comparison, allocations_df)
            st.download_button(
                label="Download PDF Report",
                data=pdf_report,
                file_name="portfolio_report.pdf",
                mime="application/pdf"
            )