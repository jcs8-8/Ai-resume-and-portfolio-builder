import streamlit as st
from logic.jd_matcher import match_resume_with_jd

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("Please login first")
    st.stop()
st.title("📊 ATS Resume Matcher")

jd = st.text_area("Paste Job Description")
resume_text = st.text_area(
    "Paste or use the last generated resume",
    st.session_state.get("resume_text", ""),
    height=220
)

if st.button("Check ATS Match"):
    score, missing = match_resume_with_jd(resume_text, jd)

    st.success(f"ATS Match Score: {score}%")
    st.warning("Missing Keywords:")
    st.write(", ".join(missing))
