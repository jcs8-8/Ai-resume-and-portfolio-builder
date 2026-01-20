import streamlit as st

from models.text_generator import load_generator
from logic.role_skills import get_role_options, get_role_skills, get_role_keywords
from logic.prompt_builder import resume_prompt
from templates.resume_template_1 import classic_template
from templates.resume_template_2 import modern_template
from utils.formatting import ensure_resume_layout
from utils.pdf_generator import generate_pdf, generate_structured_resume_pdf
from utils.version_history import save_resume_version


# ---------------- AUTH CHECK ----------------
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("🔐 Please login to access Resume Builder")
    st.stop()

user_email = st.session_state.user_email


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Builder",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Builder")
st.caption("Generate ATS-friendly, role-specific resumes using AI")


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙ Settings")

    role = st.selectbox(
        "Target Job Role",
        get_role_options()
    )

    template = st.radio(
        "Resume Template",
        ["Classic ATS", "Modern"]
    )

    tone = st.selectbox(
        "Resume Tone",
        ["Professional", "Formal", "Friendly"]
    )

    include_keywords = st.checkbox("Add ATS keyword boosters", value=True)


# ---------------- MAIN FORM ----------------
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Full Name")
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL")

with col2:
    education = st.text_area("Education", height=120)
    experience = st.text_area("Experience", height=120)

projects = st.text_area("Projects", height=120)

skills = st.text_area(
    "Skills (auto-filled based on role)",
    ", ".join([*get_role_skills(role), *(get_role_keywords(role) if include_keywords else [])]),
    height=80
)


# ---------------- GENERATE RESUME ----------------
if st.button("🚀 Generate Resume", use_container_width=True):
    if not name or not education or not skills:
        st.warning("Please fill required fields (Name, Education, Skills)")
        st.stop()

    with st.spinner("Generating professional resume..."):
        generator = load_generator()

        resume_data = {
            "name": name,
            "email": user_email,
            "linkedin": linkedin,
            "github": github,
            "education": education,
            "experience": experience,
            "projects": projects,
            "skills": skills,
            "tone": tone
        }

        # Save for Job Email page
        st.session_state.resume_data = resume_data

        # Template selection
        base_resume = (
            classic_template(resume_data)
            if template == "Classic ATS"
            else modern_template(resume_data)
        )

        # AI enhancement
        final_resume = generator(
            resume_prompt(base_resume),
            max_new_tokens=350,
            temperature=0.7,
            do_sample=True
        )[0]["generated_text"]
        final_resume = ensure_resume_layout(resume_data, final_resume)

    # ---------------- OUTPUT ----------------
    st.subheader("📄 Generated Resume")
    st.text(final_resume)

    # Keep latest resume text for other pages (ATS matcher, emails)
    st.session_state.resume_text = final_resume

    # Save version
    filename = save_resume_version(user_email, final_resume)
    st.success(f"Resume saved: {filename}")

    # Generate PDF
    generate_structured_resume_pdf(resume_data, "resume.pdf")

    st.download_button(
        "⬇ Download Resume PDF",
        data=open("resume.pdf", "rb"),
        file_name="resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )

