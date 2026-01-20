def classic_template(data):
    return f"""
{data['name']}
Email: {data['email']} | LinkedIn: {data['linkedin']} | GitHub: {data['github']}

EDUCATION
{data['education']}

SKILLS
{data['skills']}

PROJECTS
{data['projects']}

EXPERIENCE
{data['experience']}
"""
