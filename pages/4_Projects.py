import streamlit as st

st.title("Technical Projects")

st.write("""
This section highlights projects that reflect my growth as an engineering student. It includes research, robotics, and accessibility-centered work that demonstrates both technical development and initiative.
""")

st.markdown("## ECE Discovery Project")
st.write("""
My ECE Discovery Project explores how engineering can be used to make communication more accessible for Deaf and hard-of-hearing users. I became interested in this area because accessibility is often treated as a secondary feature, even though it determines whether people can fully participate in education, digital media, and everyday interaction.

My project focuses on the idea that communication tools should be designed around users rather than asking users to adapt to systems that were not built with them in mind. Through this work, I examined how software, AI, and visual systems could help translate spoken or written content into more accessible forms. Because this feature is still developing, I plan to keep refining both the technical concept and the way I present it before the Discovery Project Showcase.
""")

st.markdown("## Medical Robotics Club")
st.image(
    "assets/Advanced-Surgical-Robotics_Mobile.png.webp",
    caption="Representative robotics visual for assistive and medical robotics",
    width="stretch",
)
st.write("""
As a software member of Team Limbo in Georgia Tech Medical Robotics, I contribute to a project focused on prosthetic hand control using EMG and joint angle data. This experience has introduced me to the challenges of working with noisy real-world signals and building models that can support nonlinear motion prediction.
""")
st.caption("Image credit: add the source here if this image is not your own.")

st.markdown("## Independent Research in Nanomedicine")
st.image(
    "assets/44222_2025_306_Fig1_HTML.png",
    caption="Representative nanomedicine visual",
    width="stretch",
)
st.write("""
In an independent research project, I led work related to a proposed treatment approach for colon adenocarcinoma using folic acid-targeted mesoporous silica nanorods loaded with beta-hydroxybutyrate. This project required technical reading, experimental planning, interdisciplinary communication, and long-term persistence.
""")
st.caption("Image credit: add the source here if this image is not your own.")

st.markdown("## Teknofest Underwater Robot")
st.image(
    "assets/sualti-01.jpg",
    caption="Underwater robot built during Teknofest Robotics",
    width="stretch",
)
st.write("""
During Teknofest Robotics, I worked on the design and development of a low-cost underwater robot. This project challenged me to think practically about both engineering performance and financial constraints. Our team redesigned portions of the hardware system and reduced the component budget significantly through more efficient choices.
""")
