from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem,
    Table,
    TableStyle,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors

def generate_pdf(text, filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    # ---- Custom Styles ----
    name_style = ParagraphStyle(
        "NameStyle",
        fontSize=20,
        spaceAfter=10,
        alignment=TA_CENTER,
        leading=24
    )

    section_style = ParagraphStyle(
        "SectionStyle",
        fontSize=13,
        spaceBefore=14,
        spaceAfter=6,
        bold=True,
        textColor="#333333"
    )

    body_style = ParagraphStyle(
        "BodyStyle",
        fontSize=10,
        spaceAfter=4,
        leading=14
    )

    story = []

    # Normalize line breaks and ensure we have at least 1 line
    lines = [ln.rstrip() for ln in (text or "").replace("\r\n", "\n").split("\n")]
    lines = lines if any(l.strip() for l in lines) else [""]

    first_non_empty_idx = next((i for i, l in enumerate(lines) if l.strip()), 0)
    first_line = lines[first_non_empty_idx].strip()

    # ---- Header ----
    # If this is a cover letter / email, the first line may be "Subject:"; don't treat it as a big name header.
    if first_line.lower().startswith("subject:"):
        story.append(Paragraph(first_line, section_style))
    else:
        story.append(Paragraph(first_line or " ", name_style))
    story.append(Spacer(1, 10))

    for line in lines[first_non_empty_idx + 1:]:
        line = line.strip()

        if not line:
            story.append(Spacer(1, 6))

        # Section headings
        elif line.isupper() and len(line) < 40:
            story.append(Spacer(1, 10))
            story.append(Paragraph(line, section_style))

        # Bullet points
        elif line.startswith("•") or line.startswith("-"):
            story.append(
                ListFlowable(
                    [ListItem(Paragraph(line[1:], body_style))],
                    bulletType="bullet"
                )
            )

        # Normal text
        else:
            story.append(Paragraph(line, body_style))

    doc.build(story)


# ---------- Structured Resume (two-column) ----------
def _bullets_from_text(text: str):
    lines = [ln.strip(" •-\t") for ln in (text or "").replace("\r\n", "\n").split("\n") if ln.strip()]
    bullets = []
    for ln in lines:
        if len(ln) > 0:
            bullets.append(ln)
    return bullets


def generate_structured_resume_pdf(data: dict, filename: str):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=32,
        leftMargin=32,
        topMargin=32,
        bottomMargin=32,
    )

    styles = getSampleStyleSheet()
    name_style = ParagraphStyle("NameStyle", fontSize=22, spaceAfter=4, alignment=TA_CENTER, leading=26)
    subtitle_style = ParagraphStyle("SubtitleStyle", fontSize=10, alignment=TA_CENTER, textColor="#555555", spaceAfter=12)

    section_head = ParagraphStyle("SectionHead", fontSize=13, spaceBefore=8, spaceAfter=4, textColor="#2c3e50", leading=16)
    bullet_style = ParagraphStyle("Bullet", fontSize=10, leading=13, spaceAfter=2)
    text_style = ParagraphStyle("Text", fontSize=10, leading=13, spaceAfter=4)

    story = []

    name = data.get("name", "")
    email = data.get("email", "")
    linkedin = data.get("linkedin", "")
    github = data.get("github", "")

    subtitle_parts = [email]
    if linkedin:
        subtitle_parts.append(linkedin)
    if github:
        subtitle_parts.append(github)
    subtitle = " | ".join([p for p in subtitle_parts if p])

    story.append(Paragraph(name, name_style))
    story.append(Paragraph(subtitle, subtitle_style))
    story.append(Spacer(1, 8))

    # Prepare columns: left (experience, projects), right (education, skills, coursework, links)
    left_flow = []
    right_flow = []

    def add_section(target, title, content, is_bullets=False):
        target.append(Paragraph(title, section_head))
        if is_bullets:
            bullets = _bullets_from_text(content)
            if bullets:
                target.append(ListFlowable([ListItem(Paragraph(b, bullet_style)) for b in bullets], bulletType="bullet"))
            else:
                target.append(Paragraph(content, text_style))
        else:
            target.append(Paragraph(content or "", text_style))
        target.append(Spacer(1, 6))

    add_section(left_flow, "EXPERIENCE", data.get("experience", ""), is_bullets=True)
    add_section(left_flow, "PROJECTS", data.get("projects", ""), is_bullets=True)

    add_section(right_flow, "EDUCATION", data.get("education", ""), is_bullets=False)
    add_section(right_flow, "SKILLS", data.get("skills", ""), is_bullets=True)
    if data.get("coursework"):
        add_section(right_flow, "COURSEWORK", data.get("coursework", ""), is_bullets=True)

    links_text = "\n".join([lnk for lnk in [linkedin, github] if lnk])
    if links_text:
        add_section(right_flow, "LINKS", links_text, is_bullets=False)

    table = Table(
        [[left_flow, right_flow]],
        colWidths=[doc.width * 0.56, doc.width * 0.44],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    story.append(table)
    doc.build(story)
