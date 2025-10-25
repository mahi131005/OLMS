"""
URL configuration for lms_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index, name='index'),
    path('webdev/',views.webdev, name='webdev'),
    path('datascience/',views.datascience, name='datascience'),
    path('mobiledev/',views.mobiledev, name='mobiledev'),
    path('aiml/',views.aiml, name='aiml'),
    path('cybersec/',views.cybersec, name='cybersec'),
    path('cloudcomp/',views.cloudcomp, name='cloudcomp'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('rts/',views.rts, name='rts'),
    path('ccl/',views.ccl, name='ccl'),
    path('csqr/',views.csqr, name='csqr'),
    path('feedback/',views.feedback_form, name='feedback'),
    path('admin-dashboard/',views.admin_dashboard, name='admin_dashboard'),
    path('status/',views.status, name='status'),
    path('export-feedback/',views.export_feedback_pdf, name='export_feedback'),
    path('chatbot/', views.chatbot_response, name='chatbot_response'),
    path('',views.landing, name='landing'),
]
