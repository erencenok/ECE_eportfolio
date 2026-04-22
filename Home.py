import streamlit as st

st.title("Technical Projects")

st.write("""
This section highlights projects that reflect my growth as an engineering student. It includes research, robotics, and accessibility-centered work that demonstrates both technical development and initiative.
""")

st.markdown("## ECE Discovery Project")
st.markdown("### Early Prototype for a Constraint-Aware Room Setup Planner")
st.caption("ECE 1100 Discovery Project — Georgia Tech")

st.write("""
My ECE Discovery Project explores how software can help users plan room setups based on fit, compatibility, and budget constraints. The inspiration came from a common frustration: buying a desk that doesn't fit, a monitor mount that's incompatible, or a cable that's too short. I wanted to understand how a digital tool could help users avoid these problems by checking physical, technical, and budget constraints before making purchases.
""")

with st.expander("💡 Project Idea — Why Room Setup Planning Is Hard"):
    st.markdown("**The Core Problem**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.error("**Mismatch Hell**\n\nProducts don't fit physically or work together.")
    with col2:
        st.warning("**Decision Paralysis**\n\nHours comparing specs with no confidence in the outcome.")
    with col3:
        st.info("**Budget Blowups**\n\nForgotten accessories and returns add up fast.")
    st.write("This was a technical exploration, not a startup — the goal was to understand how software can model real-world constraints and guide better decisions.")

with st.expander("🔧 What I Built — The Early Prototype"):
    st.write("I built a small app mockup that explored a user flow where someone could define room constraints, select setup needs, and receive more informed setup recommendations.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**📷 Room Scan**")
        st.write("Capture space via camera or manual measurements.")
        st.markdown("**📦 AR Placement**")
        st.write("Drag products at true scale with clearance checks.")
    with col2:
        st.markdown("**🔌 Compatibility Checks**")
        st.write("VESA fit, cable reach, power load constraints.")
        st.markdown("**💰 Budget-Aware Recommendations**")
        st.write("Budget / Balanced / Premium tiers, all within limits.")

with st.expander("📈 Project Progress — How It Evolved"):
    st.markdown("""
    1. **Initial Idea** — Identified the room setup problem; defined core constraints to address.
    2. **Interface Planning** — Sketched user flows; mapped out constraint categories and UI screens.
    3. **Early Prototype** — Built a working mockup with room scan, placement, and recommendation logic.
    4. **Testing & Iteration** — Ran early tests; identified instability and logic gaps; iterated on design.
    """)
    st.info("This was an exploratory build. The prototype was partial — not every feature worked reliably, and that was part of the learning process.")

with st.expander("✅ Successes"):
    st.markdown("""
    - **Concept → Prototype** — Translated an abstract idea into a tangible, interactive prototype.
    - **Real-World User Flow** — Created a structured user flow that addressed a genuine everyday problem.
    - **Multi-Constraint Thinking** — Explored how physical, technical, and budget constraints interact in software decisions.
    - **System-Level Design** — Improved ability to think about user needs and system architecture together.
    """)

with st.expander("⚠️ Failures & Challenges"):
    st.markdown("""
    - **Prototype Instability** — The prototype was limited and sometimes unstable across different test cases.
    - **Logic Consistency** — Some technical logic, especially compatibility checks, was difficult to implement consistently.
    - **Connecting the Layers** — Linking room constraints, compatibility logic, and interface behavior proved harder than expected.
    """)
    st.write("Moving from concept to dependable software requires far more iteration and technical depth than initially expected. These challenges were the most valuable part of the learning process.")

with st.expander("🛠️ ECE Skills Gained"):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Software Prototyping** — Building a functional app mockup from scratch.")
        st.markdown("**System Decomposition** — Breaking a large problem into smaller, manageable components.")
        st.markdown("**Constraint-Based Thinking** — Modeling physical, technical, and budget constraints in software.")
    with col2:
        st.markdown("**Interface & Workflow Design** — Designing intuitive user flows for a multi-step process.")
        st.markdown("**Iterative Debugging** — Testing, identifying failures, and refining the prototype.")
        st.markdown("**User-Centered Engineering** — Connecting technical decisions with real practical needs.")

with st.expander("💭 Final Reflection"):
    st.markdown("> *\"Even an incomplete prototype can teach a lot about technical complexity.\"*")
    st.markdown("""
    - **Engineering Ideas Evolve** — This project showed how ideas change and improve through experimentation and honest iteration.
    - **Complexity Is Real** — Translating a concept into reliable software is far more nuanced than it first appears.
    - **Strengthened Interests** — The project deepened my interest in software, design, and problem-solving within engineering.
    - **Next Steps** — If continued: improve prototype stability and make fit/compatibility logic more robust and consistent.
    """)

st.divider()

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
