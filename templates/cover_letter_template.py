def format_cover_letter(text):
    lines = text.split("\n")
    cleaned = [l.strip() for l in lines if l.strip()]
    return "\n".join(cleaned)


COVER_LETTER_TEMPLATES = {
    "Classic (3–4 paragraphs)": "classic",
    "Impact-first (metrics)": "impact",
    "Intern / Fresher": "fresher",
    "Referral / Networking": "referral",
}