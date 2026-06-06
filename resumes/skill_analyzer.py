SKILLS = [
    "Python",
    "Django",
    "SQL",
    "Machine Learning",
    "Data Analysis",
    "Pandas",
    "NumPy",
    "HTML",
    "CSS",
    "JavaScript",
    "Git",
    "Excel"
]

def extract_skills(text):
    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


def calculate_score(skills):
    score = len(skills) * 10

    if score > 100:
        score = 100

    return score
def get_suggestions(skills):
    suggestions = []

    if "SQL" not in skills:
        suggestions.append("Learn SQL and add it to your resume.")

    if "Git" not in skills:
        suggestions.append("Add Git/GitHub skills and project links.")

    if "Django" not in skills:
        suggestions.append("Build a Django project and include it.")

    if "Pandas" not in skills:
        suggestions.append("Learn Pandas for Data Analysis.")

    if "NumPy" not in skills:
        suggestions.append("Learn NumPy for numerical computing.")

    if "Data Analysis" not in skills:
        suggestions.append("Add a Data Analysis project.")

    return suggestions

def match_jobs(skills):
    jobs = []

    if "Python" in skills:
        jobs.append(("Python Developer", 90))

    if "Machine Learning" in skills:
        jobs.append(("Machine Learning Intern", 85))

    if "HTML" in skills and "CSS" in skills and "JavaScript" in skills:
        jobs.append(("Frontend Developer", 75))

    if "Excel" in skills:
        jobs.append(("Data Analyst", 80))

    return jobs

def advanced_score(text, skills):
    score = 0

    # Skills score
    score += min(len(skills) * 10, 60)

    # Projects
    if "project" in text.lower():
        score += 20

    # Education
    if "education" in text.lower():
        score += 10

    # Contact information
    if "@" in text:
        score += 10

    return min(score, 100)

def missing_skills(skills):
    required = [
        "Python",
        "SQL",
        "Git",
        "Django",
        "Pandas",
        "NumPy",
        "Machine Learning"
    ]

    missing = []

    for skill in required:
        if skill not in skills:
            missing.append(skill)

    return missing
def ats_score(text):
    score = 0

    checks = {
        "Contact Information": "@" in text,
        "Education": "education" in text.lower(),
        "Projects": "project" in text.lower(),
        "Skills": "skills" in text.lower(),
        "LinkedIn": "linkedin" in text.lower(),
        "Certifications": "certification" in text.lower(),
    }

    for value in checks.values():
        if value:
            score += 15

    return score, checks

def career_predictions(skills):

    if "Machine Learning" in skills:
        return "Machine Learning Engineer"

    elif "Python" in skills:
        return "Python Developer"

    elif "JavaScript" in skills:
        return "Frontend Developer"

    elif "Excel" in skills:
        return "Data Analyst"

    return "Software Developer"




