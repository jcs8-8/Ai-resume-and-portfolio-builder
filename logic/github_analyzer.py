def analyze_github(repo_url):
    repo_name = repo_url.rstrip("/").split("/")[-1]

    bullets = [
        f"Developed {repo_name} project using industry-standard practices",
        "Implemented modular and scalable code architecture",
        "Applied version control and documentation best practices"
    ]

    return bullets
