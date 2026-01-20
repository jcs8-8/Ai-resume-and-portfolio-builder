from __future__ import annotations


def email_template_short(*, subject: str, body: str) -> str:
    return f"""Subject: {subject}

{body}
"""


def email_template_bullet(*, subject: str, greeting: str, bullets: list[str], closing: str) -> str:
    bullet_lines = "\n".join([f"- {b}" for b in bullets if b.strip()])
    return f"""Subject: {subject}

{greeting}

Highlights:
{bullet_lines}

{closing}
"""


EMAIL_TEMPLATES = {
    "Short & Formal": "short_formal",
    "Bullets (ATS-friendly)": "bullet",
    "Referral / Networking": "referral",
    "Follow-up After Applying": "follow_up",
}

