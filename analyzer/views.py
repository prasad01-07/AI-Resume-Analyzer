
from django.http import HttpResponse
from .utils import extract_text_from_pdf

def analyze_resume(request, resume_path):
    text = extract_text_from_pdf(resume_path)

    return HttpResponse(
        f"<h2>Extracted Resume Text</h2><pre>{text}</pre>"
    )