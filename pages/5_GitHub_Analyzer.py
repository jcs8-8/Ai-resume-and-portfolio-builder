import streamlit as st
from logic.github_analyzer import analyze_github

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("Please login first")
    st.stop()
st.title("🧑‍💻 GitHub Project Analyzer")

repo = st.text_input("GitHub Repository URL")

if repo:
    bullets = analyze_github(repo)
    for b in bullets:
        st.write("•", b)
