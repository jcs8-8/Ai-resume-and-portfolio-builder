import streamlit as st
from utils.version_history import load_resume_versions

# -------------------------------------------------
# 🔒 Authentication Check
# -------------------------------------------------
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("Please login first")
    st.stop()

if "user_email" not in st.session_state:
    st.error("Session expired. Please login again.")
    st.stop()

email = st.session_state.user_email
fullname = st.session_state.get("user_fullname", "")

# -------------------------------------------------
# 📊 Dashboard UI
# -------------------------------------------------
st.title("🎯 Dashboard")
st.subheader(f"Welcome 👋 {fullname}")
st.write(f"Logged in as **{email}**")

st.divider()

# -------------------------------------------------
# 📂 Load User Resume Versions
# -------------------------------------------------
resumes = load_resume_versions(email)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Resumes Created", len(resumes))

with col2:
    st.metric("✉️ Cover Letters", "Coming Soon")

with col3:
    st.metric("🌐 Portfolio Pages", "Coming Soon")

st.divider()

# -------------------------------------------------
# ⚡ Quick Actions
# -------------------------------------------------
st.subheader("Quick Actions")

st.page_link("pages/1_Resume_Builder.py", label="📝 Build Resume")
st.page_link("pages/2_Cover_Letter.py", label="✉️ Cover Letter")
st.page_link(
    "pages/6_Portfolio_Generator.py",
    label="🌐 Portfolio"
)

st.page_link("pages/7_Version_History.py", label="📂 Resume History")

st.divider()

# -------------------------------------------------
# 🚪 Logout
# -------------------------------------------------
if st.button("Logout"):
    st.session_state.authenticated = False
    st.session_state.user_email = None
    st.session_state.user_fullname = None
    st.rerun()
