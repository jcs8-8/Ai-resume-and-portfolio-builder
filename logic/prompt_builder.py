# -------- Resume Prompt --------
def resume_prompt(data):
    """
    Accepts:
    - formatted resume STRING
    OR
    - resume DATA dictionary
    """

    # If already formatted resume (string)
    if isinstance(data, str):
        return f"""
Improve the following resume to be ATS-friendly.

Rules:
- Keep clear section headings
- Use bullet points
- Professional wording
- One-page resume

Resume:
{data}
"""

    # If resume data dictionary
    return f"""
Create a professional ATS-friendly resume.

FORMAT STRICTLY LIKE THIS:

NAME
{data.get('name', '')}

CONTACT
Email: {data.get('email', '')}
LinkedIn: {data.get('linkedin', '')}
GitHub: {data.get('github', '')}

SKILLS
{data.get('skills', '')}

EXPERIENCE
{data.get('experience', '')}

PROJECTS
{data.get('projects', '')}

EDUCATION
{data.get('education', '')}

Rules:
- Use bullet points
- Clear spacing
- Professional language
- ATS optimized
"""

def email_prompt(resume_data, company, job_role):
    return f"""
Write a professional job application email.

Candidate Name: {resume_data.get('name', '')}
Candidate Skills:
{resume_data.get('skills', '')}

Applying For Role: {job_role}
Company Name: {company}

Rules:
- Formal tone
- Short and clear
- Include subject line
- Professional closing
"""


def email_prompt_v2(
    *,
    company: str,
    job_role: str,
    user_name: str,
    email: str,
    linkedin: str = "",
    github: str = "",
    skills: str = "",
    template_name: str = "Short & Formal",
) -> str:
    return f"""
Write a professional job application email using the template style: {template_name}.

Candidate Name: {user_name}
Candidate Email: {email}
LinkedIn: {linkedin}
GitHub/Portfolio: {github}

Applying For Role: {job_role}
Company Name: {company}

Key Skills (ATS keywords, keep concise):
{skills}

Rules:
- Include a clear Subject line starting with "Subject:"
- Keep it 120-180 words unless the template asks for bullets
- Use a professional greeting and closing
- Mention 2-4 most relevant skills for {job_role}
"""