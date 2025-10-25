from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from application.models import Feedback
from unittest.mock import patch
from django.http import JsonResponse


class TestViews(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.superuser = User.objects.create_superuser(username="admin", password="password123")
        self.client = Client()

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

        # Test POST request to sign up a new user
        response = self.client.post(reverse('signup'), data={
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertRedirects(response, reverse('index'))
        new_user = User.objects.get(username='newuser')
        self.assertTrue(new_user)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        # Test POST request for login
        response = self.client.post(reverse('login'), data={
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertRedirects(response, reverse('index'))

    def test_logout_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('landing'))

    def test_feedback_form(self):
        # Test GET request
        response = self.client.get(reverse('feedback_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback.html')

        # Test POST request with valid data
        data = {
            'student_name': 'John Doe',
            'email': 'john@example.com',
            'course_name': 'Django Basics',
            'course_rating': 5,
            'content_relevance': 'High',
            'interface_rating': 5,
            'best_feature': 'Clear explanations',
            'additional_feedback': 'None'
        }
        response = self.client.post(reverse('feedback_form'), data=data)
        self.assertRedirects(response, reverse('status'))

    def test_feedback_admin_dashboard(self):
        self.client.login(username="admin", password="password123")
        Feedback.objects.create(
            student_name='John Doe', email='john@example.com', course_name='Django Basics',
            course_rating=5, content_relevance='High', interface_rating=5,
            best_feature='Clear explanations', additional_feedback='None'
        )
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_dashboard.html')
        self.assertContains(response, 'John Doe')

    def test_admin_dashboard_permission(self):
        # Test that non-admin users cannot access the admin dashboard
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 403)

    @patch('application.gemini_utilities.get_gemini_response')
    def test_chatbot_response(self, mock_get_gemini_response):
        mock_get_gemini_response.return_value = "Mocked Gemini Response"
        
        response = self.client.post(reverse('chatbot_response'), data={'message': 'Hello'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['response'], "Mocked Gemini Response")

    def test_export_feedback_pdf(self):
        self.client.login(username="admin", password="password123")

        # Test the PDF export
        response = self.client.get(reverse('export_feedback_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

    @patch('application.gemini_utilities.model.generate_content')
    def test_get_gemini_response(self, mock_generate_content):
        mock_generate_content.return_value.text = "Mocked response text"
        response = self.client.get(reverse('chatbot_response'))
        self.assertEqual(response.status_code, 400)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_landing_view(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page.html')
