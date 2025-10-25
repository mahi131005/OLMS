from django.db import models
from django.utils.timezone import now

class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    course_name = models.CharField(max_length=150)
    course_rating = models.IntegerField()  # Rating 1-5
    content_understandability = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    content_relevance = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    content_suggestions = models.TextField(blank=True)
    interface_rating = models.IntegerField()  # Rating 1-5
    technical_issues = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    issue_details = models.TextField(blank=True)
    navigation_easy = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    usability_suggestions = models.TextField(blank=True)
    recommend = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    best_feature = models.TextField(blank=True)
    additional_feedback = models.TextField(blank=True)
    # submission_date = models.DateTimeField(default=now)  Auto-generated timestamp

    def __str__(self):
        return f"{self.student_name}"