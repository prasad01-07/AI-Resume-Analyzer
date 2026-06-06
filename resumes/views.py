from django.http import HttpResponse
from reportlab.pdfgen import canvas

from django.shortcuts import render
from .forms import ResumeForm
from analyzer.utils import extract_text_from_pdf
from .skill_analyzer import (
    extract_skills,
    advanced_score,
    get_suggestions,
    match_jobs,
    missing_skills,
    career_predictions,
    )


def home(request):
    extracted_text = ""
    skills = []
    score = 0
    suggestions = []
    jobs = []
    missing = []
    badge = ""
    career =""
    ats = 0
    ats_checks = {}

    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():
            resume = form.save()

            pdf_path = resume.resume_file.path
            extracted_text = extract_text_from_pdf(pdf_path)

            skills = extract_skills(extracted_text)
            score = advanced_score(extracted_text, skills)
            suggestions = get_suggestions(skills)
            jobs = match_jobs(skills)
            missing = missing_skills(skills)
            career = career_predictions(skills)

            # ATS Score Calculation
            ats_checks = {
                "Email Found": "@" in extracted_text,
                "Skills Section": len(skills) > 0,
                "Projects Section": "project" in extracted_text.lower(),
                "Education Section": "education" in extracted_text.lower(),
                "Resume Length": len(extracted_text) > 500,
            }

            ats = sum(ats_checks.values()) * 20

            if score >= 80:
                badge = "Excellent"
            elif score >= 60:
                badge = "Good"
            else:
                badge = "Needs Improvement"

            # Save data for PDF
            request.session["score"] = score
            request.session["badge"] = badge
            request.session["skills"] = skills
            request.session["suggestions"] = suggestions
            request.session["jobs"] = jobs
            request.session["missing"] = missing
            request.session["ats"] = ats

    else:
        form = ResumeForm()

    return render(
        request,
        "home.html",
        {
            "form": form,
            "text": extracted_text,
            "skills": skills,
            "score": score,
            "suggestions": suggestions,
            "jobs": jobs,
            "missing": missing,
            "badge": badge,
            "career": career,
            "ats": ats,
            "ats_checks": ats_checks,
        }
    )


def download_report(request):

    score = request.session.get("score", 0)
    badge = request.session.get("badge", "")
    skills = request.session.get("skills", [])
    suggestions = request.session.get("suggestions", [])
    jobs = request.session.get("jobs", [])
    missing = request.session.get("missing", [])
    ats = request.session.get("ats", 0)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="resume_report.pdf"'

    p = canvas.Canvas(response)

    y = 800

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "AI Resume Analyzer Report")

    y -= 40
    p.setFont("Helvetica", 12)
    p.drawString(50, y, f"Resume Score: {score}/100")

    y -= 20
    p.drawString(50, y, f"ATS Score: {ats}/100")

    y -= 20
    p.drawString(50, y, f"Badge: {badge}")

    y -= 40
    p.drawString(50, y, "Detected Skills:")

    for skill in skills:
        y -= 20
        p.drawString(70, y, f"- {skill}")

    y -= 40
    p.drawString(50, y, "Missing Skills:")

    for skill in missing:
        y -= 20
        p.drawString(70, y, f"- {skill}")

    y -= 40
    p.drawString(50, y, "Recommended Jobs:")

    for job in jobs:
        y -= 20
        p.drawString(70, y, f"- {job[0]}")

    y -= 40
    p.drawString(50, y, "Suggestions:")

    for suggestion in suggestions:
        y -= 20
        p.drawString(70, y, f"- {suggestion}")

    p.save()

    return response 