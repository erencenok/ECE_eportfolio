import streamlit as st

st.title("Resume")

st.write("""
My resume highlights experience across software, research, engineering projects, and student involvement. It reflects both technical development and initiative, from research and robotics to accessibility and entrepreneurship.
""")

with open("assets/CV_ErenCetinok.pdf", "rb") as file:
    st.download_button(
        label="Download Resume PDF",
        data=file,
        file_name="CV_ErenCetinok.pdf",
        mime="application/pdf"
    )

st.markdown("### Education")
st.markdown("""
**Georgia Institute of Technology**  
B.S. in Computer Engineering, expected May 2029

**Bahcesehir Science and Technology High School**  
Izmir, Turkey • GPA: 97/100 • AP Scholar with Honor
""")

st.markdown("### Highlights")
st.markdown("""
- Software member on a prosthetic-hand control project in GT Medical Robotics
- Led nanomedicine research on colon adenocarcinoma treatment design
- Summer intern at Monrol Nuclear Products working on Python and Excel-based automation
- Founder and President of Ecoquerencia, connecting students through sustainability initiatives
""")