import streamlit as st

st.title("My Portfolio Blog")
st.write("""
Welcome to my portfolio blog! Here, I share insights and details about my projects, showcasing my skills in data science, web scraping, and financial analysis. 
Explore my work and learn about the technologies and approaches I use to solve real-world problems.
""")


# Create Tabs
article_keys = [
    "Empowering Financial Insights",
    "Otodom Scraper Project",
    "Housing Price Prediction"
]
tabs = st.tabs(article_keys)

# Display content in each tab
with tabs[0]:
    st.title("My Stock Portfolio Analyzer Project")

    st.write("""
        In today's fast-paced world, making informed decisions is crucial, whether in our professional or personal lives. 
        My Stock Portfolio Analyzer project is a testament to the power of data-driven insights, particularly in the realm of personal finance.

        This project is a Python-based application designed to provide a clear and comprehensive view of stock portfolio performance. 
        It's about taking the complexity out of investment analysis and making it accessible.
    """)

    st.header("The Project's Core Strengths")

    st.write("""
        At its foundation, this tool leverages readily available financial data to provide users with a holistic picture of their investment portfolio. Here’s what it offers:
    """)

    st.markdown("""
        * **Performance Tracking:**
            * The application calculates key performance indicators, giving users a clear understanding of how their investments are performing.
            * It compares portfolio performance against market benchmarks, providing context and perspective.
        * **Risk Assessment:**
            * The tool analyzes portfolio volatility, helping users understand the level of risk associated with their investments.
            * This allows for better risk management.
        * **Data-Driven Insights:**
            * By incorporating technical indicators, the application provides users with data-driven insights that can inform their investment decisions.
        * **Accessible Reporting:**
            * The project generates easy-to-understand reports in both Excel and PDF formats, making it simple to review and share portfolio performance.
            * Visualizations are also generated, for easy comprehension.
    """)

    st.header("Why This Project Matters")

    st.write("""
        Whether you're a seasoned investor or just starting out, understanding your portfolio's performance is essential. This tool helps users:
    """)

    st.markdown("""
        * **Gain Clarity:** Simplify complex financial data and gain a clear understanding of investment performance.
        * **Make Informed Decisions:** Use data-driven insights to make smarter investment choices.
        * **Track Progress:** Easily monitor portfolio performance over time.
    """)

    st.header("The Technology Behind the Project")

    st.write("""
        The project is built using Python and leverages popular libraries like `yfinance`, `pandas`, `matplotlib`, `plotly` and `fpdf`. 
        This foundation allows for efficient data processing, analysis, and reporting.
    """)

    st.write("""
        Key technical aspects include:
    """)

    st.markdown("""
        * **Data Acquisition:** Seamlessly fetching financial data from reliable sources.
        * **Data Analysis:** Performing calculations and generating key performance metrics.
        * **Reporting and Visualization:** Creating clear and concise reports and graphs.
    """)

    st.write("### Technical Flow Chart")
    with st.expander("View Technical Flow Chart"):
        st.image("./assets/StockFlow.png", use_container_width=True, caption="Stock Code Logic Flow")


    st.header("My Approach")

    st.write("""
        This project reflects my commitment to using technology to solve real-world problems. It's about turning data into actionable insights and empowering individuals to make better decisions.

        I believe in continuous improvement, and I plan to further enhance this project with additional features and functionalities.
    """)

    st.write("""
        I invite you to explore the project's code on my GitHub repository: [Stock Portfolio Analyzer](https://github.com/KevinVanWallendael/StockPortfolioAnalyzer).
    """)
    st.write("""I welcome your feedback and contributions.""")

with tabs[1]:
    st.title("Unlocking Warsaw's Real Estate Market")

    st.write("""
        Real estate data is a goldmine for insights, whether you're a potential buyer, an investor, or simply curious about market trends. 
        To explore the Warsaw apartment market, I developed a Python-based web scraper that efficiently gathers data from Otodom.pl, a popular Polish real estate portal.
    """)

    st.header("Project Overview")

    st.write("""
        This project leverages Selenium and WebDriver Manager to automate browsing and data extraction from Otodom.pl. 
        It navigates through multiple pages of apartment listings in Warsaw, Mazowieckie, and collects key information such as price, location, size, and property features.
    """)

    st.subheader("Key Features:")
    st.markdown("""
        * **Automated Data Collection:** Uses Selenium to simulate user interaction, handling dynamic content and cookie consent popups.
        * **Comprehensive Data Extraction:** Scrapes essential details like price, title, location, size, number of rooms, and various property features.
        * **Data Storage:** Saves the scraped data in both CSV and JSON formats for easy analysis and manipulation.
        * **Efficient Navigation:** Navigates through multiple pages of listings, maximizing data collection.
    """)

    st.header("Why This Project Matters")

    st.write("""
        Understanding the real estate market requires access to accurate and up-to-date data. This project provides:
    """)

    st.markdown("""
        * **Market Insights:** Offers a snapshot of apartment listings in Warsaw, enabling analysis of pricing trends and property features.
        * **Data Accessibility:** Provides data in structured formats (CSV and JSON) for further analysis using tools like Excel, Pandas, or data visualization libraries.
        * **Automation Skills:** Demonstrates proficiency in web scraping and automation using Selenium, a valuable skill in data-driven projects.
    """)

    st.header("Technical Implementation")

    st.write("""
        The script utilizes Python with the following libraries:
    """)

    st.markdown("""
        * **Selenium:** For web browser automation and interaction.
        * **WebDriver Manager:** To automatically manage ChromeDriver installation.
        * **CSV and JSON:** For data storage and serialization.
    """)

    st.write("""
        The script is designed to handle dynamic content and cookie consent popups, ensuring robust and reliable data collection. It iterates through specified pages, extracts relevant data from each listing, and saves it to the specified files.
    """)

    st.header("My Approach")

    st.write("""
        This project showcases my ability to develop automated solutions for data collection. I focused on creating a script that is robust, efficient, and easy to maintain. 
        I believe in the power of automation to streamline data collection and analysis, enabling informed decision-making.
    """)

    st.write("""
        You can find the code for this project on my GitHub repository: [Otodom Scraper](https://github.com/KevinVanWallendael/OtodomScraper).
    """)
    st.write("""I welcome your feedback and contributions.""")

with tabs[2]:
    st.title("Predicting Warsaw Housing Prices")

    st.write("""
        For this project, I delved into the world of machine learning to build a housing price prediction model for Warsaw, Poland. 
        Using data scraped from Otodom.pl with Selenium, I aimed to create a robust model that accurately predicts apartment prices based on various features.
    """)

    st.header("Project Overview")

    st.write("""
        This project involved a comprehensive data science workflow, from data collection and preprocessing to model training and evaluation. 
        The dataset, containing information on property details such as size, rent, location, and amenities, was meticulously cleaned and transformed to prepare it for machine learning.
    """)

    st.subheader("Key Steps:")
    st.markdown("""
        * **Data Collection:** Scraped data from Otodom.pl using Selenium (see my Otodom Scraper project: [Otodom Scraper](https://github.com/KevinVanWallendael/OtodomScraper)).
        * **Data Preprocessing:** Cleaned and transformed the data, handling missing values, outliers, and formatting issues.
        * **Feature Engineering:** Created new features like price per square meter and binary amenity indicators.
        * **Model Training:** Trained an XGBoost regression model using the preprocessed data.
        * **Model Evaluation:** Evaluated the model's performance using appropriate metrics.
    """)

    st.header("Data Preprocessing and Feature Engineering")

    st.write("""
        A significant portion of the project focused on data preprocessing. Key steps included:
    """)

    st.markdown("""
        * **Cleaning 'size' and 'Czynsz' columns:** Removing units and formatting issues, converting to numeric types.
        * **Handling missing values:** Imputing missing values and creating a missing indicator for 'Czynsz'.
        * **Extracting location information:** Deriving city, neighborhood, and region from the location column.
        * **Preprocessing the 'price' column:** Removing currency symbols and handling unavailable price information.
        * **Creating 'price per square meter':** A crucial feature for understanding pricing dynamics.
        * **Extracting amenities:** Creating binary features for amenities like balcony, garage, etc.
        * **Removing outliers:** Using the IQR method to ensure robust model performance.
        * **Log transforming the target variable:** Reducing skewness in the 'price' distribution.
    """)

    st.header("Model Training and Evaluation")

    st.write("""
        I used XGBoost, a powerful gradient boosting algorithm, for the regression task. The model pipeline included preprocessing steps and the XGBoost regressor. The dataset was split into training and testing sets to evaluate the model's generalization performance.
    """)

    st.write("""
        Key aspects of the model training included:
    """)
    st.markdown("""
        * **Preprocessing pipelines:** Separate pipelines for numerical and categorical features.
        * **XGBoost regressor:** Tuned with parameters like `n_estimators`, `learning_rate`, and `max_depth`.
        * **Model evaluation:** Using metrics like Mean Absolute Error (MAE) to assess prediction accuracy.
    """)

    st.header("My Approach and Insights")

    st.write("""
        This project allowed me to apply my knowledge of machine learning to a real-world problem. I learned the importance of thorough data preprocessing and feature engineering in building accurate predictive models. 
        XGBoost proved to be a powerful tool for this regression task, demonstrating its ability to handle complex datasets and provide accurate predictions.
    """)

    st.write("""
        You can find the code for this project on my GitHub repository: [Housing Price Prediction](https://github.com/KevinVanWallendael/HousingPricePrediction).""")
    st.write("""I welcome your feedback and contributions.""")