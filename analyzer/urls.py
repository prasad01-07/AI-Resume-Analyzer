from django.urls import path
from .views import analyze_resume

urlpatterns = [
    path('analyze/<path:resume_path>/', analyze_resume, name='analyze_resume'),
]