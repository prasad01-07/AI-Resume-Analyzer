from django.contrib import admin
from django.urls import path
from resumes.views import home, download_report

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path(
        'download-report/',
        download_report,
        name='download_report'
    ),
]