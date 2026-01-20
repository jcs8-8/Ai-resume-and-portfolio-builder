"""
Lightweight formatting utilities to keep AI outputs readable/ATS-friendly.
"""

from __future__ import annotations
from datetime import datetime


def _normalize(text: str) -> str:
    return (text or "").replace("\r\n", "\n").strip()


def _has_enough_structure(text: str) -> bool:
    """
    Heuristic: treat as poorly formatted if too few line breaks.
    """
    lines = _normalize(text).split("\n")
    non_empty = [l for l in lines if l.strip()]
    return len(non_empty) >= 8  # at least a few sections/lines


def _bulletize_csv(csv_text: str) -> str:
    parts = [p.strip() for p in (csv_text or "").replace("\n", ",").split(",") if p.strip()]
    return "\n".join([f"• {p}" for p in parts])


def build_structured_resume(data: dict) -> str:
    """Deterministic, ATS-friendly structure as a fallback."""
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    linkedin = data.get("linkedin", "").strip()
    github = data.get("github", "").strip()
    education = data.get("education", "").strip()
    experience = data.get("experience", "").strip()
    projects = data.get("projects", "").strip()
    skills = _bulletize_csv(data.get("skills", ""))

    return f"""\
{name}
Email: {email}
LinkedIn: {linkedin}
GitHub: {github}

SKILLS
{skills}

EXPERIENCE
{experience}

PROJECTS
{projects}

EDUCATION
{education}
"""


def ensure_resume_layout(resume_data: dict, ai_text: str) -> str:
    """
    If the AI output collapses into one line or loses structure,
    fall back to a clean, sectioned layout.
    """
    normalized = _normalize(ai_text)
    if _has_enough_structure(normalized):
        return normalized
    return build_structured_resume(resume_data)


# -------- Cover Letter formatting --------
def build_structured_cover_letter(resume_data: dict, role: str, body: str) -> str:
    name = resume_data.get("name", "").strip()
    email = resume_data.get("email", "").strip()
    linkedin = resume_data.get("linkedin", "").strip()
    github = resume_data.get("github", "").strip()
    today = datetime.now().strftime("%d %B %Y")

    contact_line = " | ".join([p for p in [resume_data.get("phone", ""), email, linkedin, github] if p])
    header = "\n".join([name, contact_line])

    subject = f"Subject: Application for {role}"

    greeting = "Dear Hiring Manager,"

    closing = f"Sincerely,\n{name}"

    return "\n\n".join([header, today, subject, greeting, body.strip(), closing])


def ensure_cover_letter_layout(resume_data: dict, role: str, ai_text: str) -> str:
    txt = _normalize(ai_text)
    has_subject = "subject:" in txt.lower()
    has_greeting = "dear " in txt.lower()
    if has_subject and has_greeting:
        return txt
    # Use AI text as body inside a clean layout
    return build_structured_cover_letter(resume_data, role, txt)


# -------- Email formatting --------
def ensure_email_layout(resume_data: dict, role: str, company: str, ai_text: str) -> str:
    txt = _normalize(ai_text)
    if "subject:" in txt.lower():
        return txt

    subject = f"Subject: Application for {role} at {company}"
    greeting = "Dear Hiring Manager,"
    signature = "\n".join(
        [resume_data.get("name", ""), resume_data.get("email", ""), resume_data.get("linkedin", ""), resume_data.get("github", "")]
    ).strip()
    return "\n\n".join([subject, greeting, txt, signature])
