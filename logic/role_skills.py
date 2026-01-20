"""
Central catalog of role-specific ATS-friendly skills/keywords.
Used by Resume Builder, Cover Letter, and Job Email pages.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RoleProfile:
    title: str
    skills: list[str]
    keywords: list[str]


ROLE_PROFILES: dict[str, RoleProfile] = {
    # --- Web / Software ---
    "Frontend Developer": RoleProfile(
        title="Frontend Developer",
        skills=[
            "HTML5", "CSS3", "JavaScript (ES6+)", "TypeScript",
            "React", "Next.js", "Redux", "Tailwind CSS",
            "Responsive Design", "Accessibility (WCAG)", "REST APIs", "Git",
        ],
        keywords=[
            "SPA", "SSR", "CSR", "Component-driven development", "Cross-browser compatibility",
            "Web performance", "Lighthouse", "Core Web Vitals", "Unit testing", "Jest", "React Testing Library",
        ],
    ),
    "Backend Developer": RoleProfile(
        title="Backend Developer",
        skills=[
            "Node.js", "Express.js", "Python", "FastAPI", "Django",
            "REST APIs", "SQL", "PostgreSQL", "MongoDB",
            "Authentication (JWT/OAuth)", "Caching (Redis)", "Git",
        ],
        keywords=[
            "Microservices", "API design", "Rate limiting", "Logging/Monitoring",
            "CI/CD", "Docker", "System design", "Performance optimization",
        ],
    ),
    "Full Stack Developer": RoleProfile(
        title="Full Stack Developer",
        skills=[
            "React", "Node.js", "Express.js", "TypeScript",
            "REST APIs", "PostgreSQL", "MongoDB",
            "Authentication (JWT/OAuth)", "Docker", "Git",
        ],
        keywords=[
            "End-to-end feature delivery", "Agile/Scrum", "CI/CD", "Cloud deployment",
            "Testing", "Debugging", "Code reviews", "Scalable architecture",
        ],
    ),
    "Web Developer": RoleProfile(
        title="Web Developer",
        skills=[
            "HTML5", "CSS3", "JavaScript", "Responsive Design",
            "React or Vanilla JS", "REST API integration", "Git",
        ],
        keywords=[
            "Cross-browser compatibility", "Performance optimization",
            "Accessibility", "SEO basics", "Deployment (Netlify/Vercel)",
        ],
    ),
    "Java Developer": RoleProfile(
        title="Java Developer",
        skills=[
            "Java", "Spring Boot", "Hibernate/JPA", "REST APIs",
            "SQL", "MySQL/PostgreSQL", "JUnit", "Maven/Gradle", "Git",
        ],
        keywords=[
            "Design patterns", "Microservices", "API integration", "Performance tuning",
            "Exception handling", "Threading/Concurrency", "CI/CD",
        ],
    ),
    "Python Developer": RoleProfile(
        title="Python Developer",
        skills=[
            "Python", "FastAPI/Django/Flask", "REST APIs",
            "SQL", "PostgreSQL", "Testing (pytest)", "Git",
        ],
        keywords=[
            "OOP", "Async programming", "Code quality", "Type hints",
            "Performance optimization", "CI/CD", "Docker",
        ],
    ),
    # --- Data / AI ---
    "Data Analyst": RoleProfile(
        title="Data Analyst",
        skills=[
            "SQL", "Excel", "Python", "Pandas",
            "Data Cleaning", "Data Visualization", "Power BI/Tableau",
            "Statistics", "Reporting", "Git",
        ],
        keywords=[
            "KPI dashboards", "ETL", "Stakeholder management", "A/B testing",
            "Data storytelling", "Business insights",
        ],
    ),
    "Data Scientist": RoleProfile(
        title="Data Scientist",
        skills=[
            "Python", "Pandas", "NumPy", "Scikit-learn",
            "Statistics", "Machine Learning", "SQL",
            "Model Evaluation", "Feature Engineering",
        ],
        keywords=[
            "Experimentation", "A/B testing", "Time series", "NLP",
            "Model deployment", "MLOps basics",
        ],
    ),
    "AI / ML Engineer": RoleProfile(
        title="AI / ML Engineer",
        skills=[
            "Python", "PyTorch/TensorFlow", "Deep Learning",
            "NLP/Computer Vision", "Model Training", "Model Serving",
            "Docker", "Git",
        ],
        keywords=[
            "MLOps", "Model monitoring", "Data pipelines", "LLMs",
            "Fine-tuning", "RAG", "Vector databases",
        ],
    ),
    "GenAI / LLM Engineer": RoleProfile(
        title="GenAI / LLM Engineer",
        skills=[
            "Python", "Prompt Engineering", "RAG", "Vector Databases (FAISS/Pinecone)",
            "LangChain/LlamaIndex", "OpenAI/HF Transformers",
            "APIs", "Docker", "Git",
        ],
        keywords=[
            "Evaluation", "Hallucination mitigation", "Embeddings", "Retrieval",
            "Guardrails", "Cost/latency optimization", "Agentic workflows",
        ],
    ),
    # --- Cloud / DevOps / QA ---
    "DevOps Engineer": RoleProfile(
        title="DevOps Engineer",
        skills=[
            "Linux", "Git", "CI/CD", "Docker", "Kubernetes",
            "AWS/Azure/GCP", "Terraform/IaC", "Monitoring (Prometheus/Grafana)",
        ],
        keywords=[
            "SRE", "Incident response", "High availability", "Auto-scaling",
            "Observability", "Security best practices",
        ],
    ),
    "Cloud Engineer": RoleProfile(
        title="Cloud Engineer",
        skills=[
            "AWS/Azure/GCP", "Networking", "IAM", "Compute/Storage",
            "Docker", "Terraform", "CI/CD", "Monitoring",
        ],
        keywords=[
            "Cloud migration", "Cost optimization", "Security", "Reliability",
            "Infrastructure automation", "Well-Architected Framework",
        ],
    ),
    "QA / Test Engineer": RoleProfile(
        title="QA / Test Engineer",
        skills=[
            "Test Planning", "Test Cases", "Bug Tracking (Jira)",
            "Manual Testing", "Automation (Selenium/Cypress)",
            "API Testing (Postman)", "SQL basics",
        ],
        keywords=[
            "Regression testing", "Smoke testing", "SDLC/STLC", "Defect lifecycle",
            "Test automation framework", "Quality metrics",
        ],
    ),
    # --- Product / Design (lightweight additions) ---
    "UI/UX Designer": RoleProfile(
        title="UI/UX Designer",
        skills=[
            "User Research", "Wireframing", "Prototyping (Figma)",
            "Information Architecture", "Usability Testing", "Design Systems",
        ],
        keywords=[
            "User flows", "Accessibility", "Heuristic evaluation",
            "Stakeholder collaboration", "Iteration",
        ],
    ),
}


def get_role_options() -> list[str]:
    return sorted(ROLE_PROFILES.keys())


def get_role_profile(role: str) -> RoleProfile | None:
    return ROLE_PROFILES.get(role)


def get_role_skills(role: str) -> list[str]:
    profile = get_role_profile(role)
    return profile.skills if profile else []


def get_role_keywords(role: str) -> list[str]:
    profile = get_role_profile(role)
    return profile.keywords if profile else []
