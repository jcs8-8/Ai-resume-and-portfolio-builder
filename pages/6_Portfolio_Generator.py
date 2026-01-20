import streamlit as st
from templates.portfolio_website import generate_portfolio_html

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("Please login first")
    st.stop()
st.title("🌐 Portfolio Website Generator")

if "resume_data" not in st.session_state:
    st.warning("Generate resume first.")
    st.stop()

html = generate_portfolio_html(st.session_state.resume_data)

st.download_button(
    "⬇ Download Portfolio Website",
    html,
    file_name="portfolio.html",
    mime="text/html"
)
