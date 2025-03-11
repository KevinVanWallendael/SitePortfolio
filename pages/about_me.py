import streamlit as st

# --- Header Section ---
col1, col2 = st.columns([1, 3], gap="medium")  
with col1:
    st.image("./assets/profile-pic.png", width=180)  

with col2:
    st.title("Kevin Van Wallendael")
    st.write("Business Intelligence Engineer")
    if st.button("✉️ Contact Me"):
        st.markdown("""
        Hello! I'm Kevin, passionate about transforming data into actionable insights.
        """)

st.markdown("---")  

# --- Introduction Section ---
st.header("About Me")
st.markdown("""
Hello! I'm Kevin Van Wallendael, a Business Intelligence Engineer with a passion for leveraging data to drive informed decisions. 
I enjoy working with data analysis, automation, and machine learning, and I'm always eager to explore new ways to solve problems. 
My experience at Amazon has provided me with valuable opportunities to develop and implement data-driven solutions that improve operational efficiency.
""")

# --- Skills & Expertise Section ---
st.header("Skills & Expertise")
skills_cols = st.columns(2) 

with skills_cols[0]:
    st.subheader("Business Intelligence & Data Warehousing")
    st.markdown("""
    * Data Pipelines & ETL
    * Dashboarding (Quicksight, Power BI, Streamlit)
    """)

    st.subheader("Automation & Optimization")
    st.markdown("""
    * Process Automation
    * Efficiency Improvements (Amazon Experience)
    """)

    st.subheader("Collaboration & Languages")
    st.markdown("""
    * Team Collaboration
    * Languages: Dutch, English, Polish
    """)


with skills_cols[1]:
    st.subheader("Data Analysis & Machine Learning")
    st.markdown("""
    * Data Visualization (Python, Power BI)
    * ML (NLP, Time Series)
    """)

    st.subheader("Cloud Platforms")
    st.markdown("""
    * AWS Infrastructure
    * Scalable Data Solutions
    """)

    st.subheader("Certifications")
    st.markdown("""
    * MicroStrategy Analyst
    * AZ-900 Azure Fundamentals
    """)

st.markdown("---")  

# --- Featured Projects Section ---
st.header("Featured Projects")
projects_cols = st.columns(3)

with projects_cols[0]:
    st.image("./assets/StockPortfolio.jpg", use_container_width=True, caption="Portfolio Analysis")  
    st.markdown(f"""
    [Portfolio Analysis](https://github.com/KevinVanWallendael/StockPortfolioAnalyzer)
    """)

with projects_cols[1]:
    st.image("./assets/Otodom.jpg", use_container_width=True, caption="Otodom Web Scraper")  
    st.markdown(f"""
    [Otodom Web Scraper](https://github.com/KevinVanWallendael/OtodomScraper)
    """)

with projects_cols[2]:
    st.image("./assets/PredictionModel.jpg", use_container_width=True, caption="Warsaw Housing Prediction") 
    st.markdown(f"""
    [Warsaw Housing Prediction](https://github.com/KevinVanWallendael/HousingPricePrediction)
    """)
st.markdown("---")  

# --- Let's Connect Section ---
st.header("Let's Connect")
contact_cols = st.columns(2)

with contact_cols[0]:
    st.markdown("""
    * **Email**: [Kevin's Mail](mailto:kev.vanwallendael@gmail.com)
    * **LinkedIn**: [Kevin's LinkedIn](https://www.linkedin.com/in/kevin-van-wallendael/)
    * **GitHub**: [Kevin's GitHub](https://github.com/KevinVanWallendael)
    """)

with contact_cols[1]:
    st.write("Looking forward to connecting!")