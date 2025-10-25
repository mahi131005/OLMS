from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            "student_name",
            "email",
            "course_name",
            "course_rating",
            "content_understandability",
            "content_relevance",
            "content_suggestions",
            "interface_rating",
            "technical_issues",
            "issue_details",
            "navigation_easy",
            "usability_suggestions",
            "recommend",
            "best_feature",
            "additional_feedback",
        ]  # Explicitly mentioning all fields (excluding timestamp)
