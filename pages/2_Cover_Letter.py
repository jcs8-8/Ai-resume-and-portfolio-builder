import streamlit as st
from models.text_generator import load_generator
from logic.cover_letter import cover_letter_prompt
from templates.cover_letter_template import format_cover_letter, COVER_LETTER_TEMPLATES
from utils.pdf_generator import generate_pdf
from logic.role_skills import get_role_options, get_role_skills, get_role_keywords
from utils.formatting import ensure_cover_letter_layout

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("Please login first")
    st.stop()
st.title("✉️ Cover Letter Generator")

if "resume_data" not in st.session_state:
    st.warning("Please generate a resume first.")
    st.stop()

role = st.selectbox("Job Role", get_role_options())
template_name = st.selectbox("Cover Letter Template", list(COVER_LETTER_TEMPLATES.keys()))
include_keywords = st.checkbox("Include ATS keywords", value=True)

if st.button("Generate Cover Letter"):
    # Validate required fields
    resume_data = dict(st.session_state.resume_data)
    if not resume_data.get("name"):
        st.warning("Your resume is missing a name. Please regenerate the resume with your name.")
        st.stop()

    role_skills = get_role_skills(role)
    role_keywords = get_role_keywords(role) if include_keywords else []
    resume_data["skills"] = ", ".join([*role_skills, *role_keywords]) or resume_data.get("skills", "")

    with st.spinner("Generating cover letter..."):
        try:
            gen = load_generator()
            text = gen(
                cover_letter_prompt(resume_data, role, template_name=template_name),
                max_new_tokens=250,
                temperature=0.7,
            )[0]["generated_text"]
            text = format_cover_letter(text)
            text = ensure_cover_letter_layout(resume_data, role, text)
        except Exception as e:
            st.error(f"Generation failed: {e}")
            st.stop()

    st.subheader("Generated Cover Letter")
    st.text_area("Cover Letter", text, height=320)

    # Persist for history
    st.session_state.cover_letter_text = text

    generate_pdf(text, "cover_letter.pdf")
    st.download_button("⬇ Download Cover Letter PDF", open("cover_letter.pdf", "rb"), "cover_letter.pdf", use_container_width=True)
