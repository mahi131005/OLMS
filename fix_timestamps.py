import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lms_project.settings")
django.setup()

from application.models import Feedback
from django.utils.timezone import localtime

for feedback in Feedback.objects.all():
    feedback.submission_date = localtime(feedback.submission_date)
    feedback.save()

print("Timestamps updated successfully!")
