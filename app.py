import streamlit as st
from modules.generator import generate_email
from modules.rewrite import rewrite_email
from modules.analyzer import analyze_email
from modules.followup import generate_followups

st.set_page_config(
    page_title="AI Email Writer",
    layout="centered"
)

st.title("📧 AI Email Writer")

tab1, tab2, tab3, tab4 = st.tabs([
    "Generate Email",
    "Rewrite Email",
    "Analyze Email",
    "Follow-up Sequence"
])

# ---------------- GENERATE ---------------- #

with tab1:

    st.header("Generate Professional Email")

    purpose = st.text_area(
        "Enter Email Purpose"
    )

    tone = st.selectbox(
        "Select Tone",
        [
            "Professional",
            "Friendly",
            "Formal",
            "Apologetic",
            "Assertive"
        ]
    )

    length = st.selectbox(
        "Select Length",
        [
            "Short",
            "Medium",
            "Detailed"
        ]
    )

    if st.button("Generate Email"):

        result = generate_email(
            purpose,
            tone,
            length
        )

        st.subheader("Generated Email")

        st.write(result)

# ---------------- REWRITE ---------------- #

with tab2:

    st.header("Rewrite Existing Email")

    old_email = st.text_area(
        "Paste Existing Email"
    )

    goal = st.selectbox(
        "Improvement Goal",
        [
            "More Professional",
            "More Concise",
            "More Persuasive",
            "Fix Grammar"
        ]
    )

    if st.button("Rewrite Email"):

        rewritten = rewrite_email(
            old_email,
            goal
        )

        st.subheader("Rewritten Email")

        st.write(rewritten)

# ---------------- ANALYZE ---------------- #

with tab3:

    st.header("Analyze Email")

    email_text = st.text_area(
        "Paste Email for Analysis"
    )

    if st.button("Analyze Email"):

        analysis = analyze_email(email_text)

        st.subheader("Analysis Result")

        st.write(
            f"Readability Score: {analysis['readability_score']}"
        )

        st.write(
            f"Reading Level: {analysis['reading_level']}"
        )

# ---------------- FOLLOWUP ---------------- #

with tab4:

    st.header("Generate Follow-up Sequence")

    context = st.text_area(
        "Enter Original Email Context"
    )

    if st.button("Generate Follow-ups"):

        followups = generate_followups(context)

        st.subheader("Follow-up Emails")

        st.write(followups)