import streamlit as st

st.set_page_config(
    page_title="Eren Cetinok | ePortfolio",
    page_icon="💼",
    layout="wide"
)

st.title("Eren Cetinok")
st.subheader("Georgia Tech • B.S. in Computer Engineering")

col1, col2 = st.columns(2)

with col1:
    st.image("assets/IMG_7171.jpg", caption="Presenting at a student event", use_container_width=True)

with col2:
    st.image("assets/main-campus.jpg", caption="Georgia Tech campus", use_container_width=True)
st.markdown("""
## Welcome

Welcome to my ePortfolio. I am Eren Cetinok, a Computer Engineering student at Georgia Tech with interests in software, AI, robotics, accessibility, and product development.

This website brings together my background, technical growth, career direction, and selected project work in one professional space. It is designed to showcase my academic development, technical interests, and long-term goals in a clear and professional format.
""")

st.markdown("### Quick Snapshot")
st.markdown("""
- B.S. in Computer Engineering, Georgia Tech, expected May 2029
- Interested in software, AI, accessibility, robotics, and product development
- Active in GT Medical Robotics, Silicon Jackets, DSGT, Product@GT, GT SCLO, and Global Leadership
""")

st.info("Use the sidebar to navigate through the ePortfolio sections.")
