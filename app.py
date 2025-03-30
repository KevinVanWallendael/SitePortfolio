import streamlit as st

about_page = st.Page(
    "pages/about_me.py",
    title="About Me",
    icon="👤",
    default=True,
)
project_1_page = st.Page(
    "pages/portfolio_analysis.py",
    title="Portfolio Analysis",
    icon="📊",
)

project_2_page = st.Page(
    "pages/assistant.py",
    title="Chatbot Assisstant",
    icon="🤖",
)

project_3_page = st.Page(
    "pages/housing_project.py",
    title="Housing Project",
    icon="🏡",
)

project_4_page = st.Page(
    "pages/blog.py",
    title="Blog",
    icon="👨🏼‍💻",
)


pg = st.navigation(
    {
        "Info": [about_page, project_4_page],
        "Projects": [project_1_page, project_3_page, project_2_page],
    }
)

st.sidebar.markdown("Made with ❤️ by [Kevin](https://www.linkedin.com/in/kevin-van-wallendael/)")

pg.run()