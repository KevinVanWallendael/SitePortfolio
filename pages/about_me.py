import streamlit as st

# --- Header Section ---
col1, col2 = st.columns([1, 3], gap="medium")
with col1:
    st.image("./assets/profile-pic.png", width=180)

with col2:
    st.title("Kevin Van Wallendael")
    st.subheader("Business Intelligence Engineer II")  
    st.write(
        "Data enthusiast | Problem solver | Always curious" 
    )
    st.markdown(
        """
        I turn data into actionable insights. Let's build something amazing together!
        """  
    )

st.markdown("---")

# --- Introduction Section ---
st.header("About Me")
st.write(
    """
    Hey there! I'm Kevin, a Business Intelligence Engineer with a knack for wrangling data and transforming it into clear, impactful stories.
    I thrive on the challenge of uncovering hidden patterns and building solutions that drive real-world improvements.
    My journey at Amazon has been an incredible learning experience, where I've honed my skills in data analysis, automation, and even a bit of machine learning.
    I'm always eager to learn, explore new technologies, and collaborate on exciting projects.
    """  
)

# --- Skills & Expertise Section ---
st.header("Skills & Expertise")
tab1, tab2 = st.tabs(["Data & BI", "Tech & Tools"])

with tab1:
    st.subheader("Business Intelligence & Data Warehousing")
    st.markdown(
        """
        * Data Pipelines & ETL
        * Dashboarding: Quicksight, Power BI, Streamlit
        * Data Visualization
        """
    )  

    st.subheader("Data Analysis & Machine Learning")
    st.markdown(
        """
        * Statistical Analysis
        * ML: NLP, Time Series Analysis
        """
    )  

with tab2:
    st.subheader("Automation & Optimization")
    st.markdown(
        """
        * Process Automation
        * Efficiency Improvements
        * Cloud Platforms: AWS Infrastructure, Scalable Data Solutions
        """
    )  

    st.subheader("Languages & Certifications")
    st.markdown(
        """
        * Languages: Dutch, English, Polish
        * Certifications: MicroStrategy Analyst, AZ-900 Azure Fundamentals
        """
    )  

st.markdown("---")

# --- Featured Projects Section ---
st.header("Featured Projects")
cols = st.columns(3)  

projects = [
    {
        "image": "./assets/StockPortfolio.jpg",
        "caption": "Portfolio Analysis",
        "url": "https://github.com/KevinVanWallendael/StockPortfolioAnalyzer",
    },
    {
        "image": "./assets/OtoDom.jpg",
        "caption": "Otodom Web Scraper",
        "url": "https://github.com/KevinVanWallendael/OtodomScraper",
    },
    {
        "image": "./assets/PredictionModel.jpg",
        "caption": "Warsaw Housing Prediction",
        "url": "https://github.com/KevinVanWallendael/HousingPricePrediction",
    },
]  

for i, project in enumerate(projects):
    with cols[i]:
        st.image(
            project["image"], use_container_width=True, caption=project["caption"]
        )
        st.markdown(f"[{project['caption']}]({project['url']})")

st.markdown("---")

# --- Let's Connect Section ---
st.header("Let's Connect!") 
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        I'm always up for a chat about data, tech, or anything interesting!
        Feel free to reach out through any of these channels:
        """  
    )
    st.markdown(
        """
        * **Email:** <a href="mailto:kev.vanwallendael@gmail.com">kev.vanwallendael@gmail.com</a>
        * **LinkedIn:** <a href="https://www.linkedin.com/in/kevin-van-wallendael/">Kevin's LinkedIn</a>
        * **GitHub:** <a href="https://github.com/KevinVanWallendael">Kevin's GitHub</a>
        """,
        unsafe_allow_html=True,
    )  

with col2:
    st.write("Looking forward to connecting!")