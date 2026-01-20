def cover_letter_prompt(data, role, template_name: str = "Classic (3–4 paragraphs)"):
    return f"""
Write a professional, ATS-friendly cover letter for the role of {role}.
Use template style: {template_name}.

Candidate Details:
Name: {data['name']}
Email: {data['email']}
Education: {data['education']}
Skills: {data['skills']}
Projects: {data['projects']}
Experience: {data['experience']}

Guidelines:
- Professional tone
- 3–4 short paragraphs unless template needs bullets
- Highlight skills relevant to {role}
- Use keywords naturally (no keyword stuffing)
- End politely
"""
