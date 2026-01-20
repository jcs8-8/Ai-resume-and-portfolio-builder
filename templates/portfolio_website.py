def generate_portfolio_html(data):
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>{data['name']} | Portfolio</title>
<style>
body {{
    font-family: Arial;
    margin: 40px;
    background-color: #f9f9f9;
}}
h1 {{ color: #2c3e50; }}
h2 {{ color: #34495e; }}
.section {{
    margin-bottom: 20px;
}}
</style>
</head>
<body>

<h1>{data['name']}</h1>
<p><b>Email:</b> {data['email']}</p>
<p>
<a href="{data['linkedin']}">LinkedIn</a> |
<a href="{data['github']}">GitHub</a>
</p>

<div class="section">
<h2>Education</h2>
<p>{data['education']}</p>
</div>

<div class="section">
<h2>Skills</h2>
<p>{data['skills']}</p>
</div>

<div class="section">
<h2>Projects</h2>
<p>{data['projects']}</p>
</div>

<div class="section">
<h2>Experience</h2>
<p>{data['experience']}</p>
</div>

</body>
</html>
"""
