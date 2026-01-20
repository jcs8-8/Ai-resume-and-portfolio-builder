import streamlit as st
import os
from utils.version_history import (
    load_resume_versions,
    load_cover_letter_versions,
    load_email_versions,
    save_resume_version,
    save_cover_letter_version,
    save_email_version,
)

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("Please login first")
    st.stop()

email = st.session_state.get("user_email", "")

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(page_title="Version History", page_icon="🗂️")

st.title("🗂️ Version History (Per User)")

st.markdown("""
View, download, and manage previously generated versions.
Saved separately per account for resume, cover letter, and job emails.
""")

st.divider()

def saver(section_title, key_name, save_fn, load_fn):
    st.subheader(section_title)
    text = st.text_area(f"Paste/confirm {section_title.lower()} to save", st.session_state.get(key_name, ""), height=220)
    if st.button(f"Save {section_title}"):
        if text.strip():
            filename = save_fn(email, text)
            st.success(f"Saved as {filename}")
        else:
            st.warning("Content cannot be empty")

    files = load_fn(email)
    if not files:
        st.info(f"No {section_title.lower()} saved yet.")
        st.divider()
        return

    selected = st.selectbox(f"Select {section_title}", files, key=f"{section_title}_select")
    file_path = os.path.join("data", "users", email, section_title.split()[0].lower() + "s", selected)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    st.text_area(f"{section_title} Preview", content, height=260)
    st.download_button(f"⬇️ Download {section_title}", data=content, file_name=selected, mime="text/plain")
    st.divider()


saver("Resume", "resume_text", save_resume_version, load_resume_versions)
saver("Cover Letter", "cover_letter_text", save_cover_letter_version, load_cover_letter_versions)
saver("Job Email", "email_text", save_email_version, load_email_versions)
