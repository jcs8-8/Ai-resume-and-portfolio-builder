import streamlit as st
from models.text_generator import load_generator
from logic.prompt_builder import email_prompt_v2
from logic.role_skills import get_role_options, get_role_skills, get_role_keywords
from utils.pdf_generator import generate_pdf
from utils.formatting import ensure_email_layout

# Authentication check
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("Please login first")
    st.stop()

st.title("📧 Job Application Email")

# Resume data check
if "resume_data" not in st.session_state:
    st.warning("Generate resume first.")
    st.stop()

company = st.text_input("Company Name")
role = st.selectbox("Role", get_role_options())
email_style = st.selectbox(
    "Email Template",
    ["Short & Formal", "Bullets (ATS-friendly)", "Referral / Networking", "Follow-up After Applying"],
)
include_keywords = st.checkbox("Include extra ATS keywords", value=True)

if st.button("Generate Email"):
    if not company.strip() or not role.strip():
        st.warning("Please provide both Company Name and Role.")
        st.stop()

    resume = st.session_state.resume_data
    if not resume.get("name"):
        st.warning("Your resume is missing a name. Please regenerate your resume first.")
        st.stop()

    role_skills = get_role_skills(role)
    role_keywords = get_role_keywords(role) if include_keywords else []
    ats_block = ", ".join([*role_skills, *role_keywords]) or resume.get("skills", "")

    with st.spinner("Generating email..."):
        try:
            gen = load_generator()
            email_text = gen(
                email_prompt_v2(
                    company=company,
                    job_role=role,
                    user_name=resume.get("name", ""),
                    email=resume.get("email", ""),
                    linkedin=resume.get("linkedin", ""),
                    github=resume.get("github", ""),
                    skills=ats_block,
                    template_name=email_style,
                ),
                max_new_tokens=180,
                temperature=0.7,
            )[0]["generated_text"]
            email_text = ensure_email_layout(resume, role, company, email_text)
        except Exception as e:
            st.error(f"Generation failed: {e}")
            st.stop()

    st.subheader("Generated Email")
    st.text_area("Email Content", email_text, height=260)

    # Persist for history
    st.session_state.email_text = email_text

    generate_pdf(email_text, "job_email.pdf")
    st.download_button("⬇ Download Email PDF", open("job_email.pdf", "rb"), "job_email.pdf", use_container_width=True)
