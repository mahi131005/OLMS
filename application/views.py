from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from application.middlewares import auth, unauth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse,JsonResponse
from .models import Feedback
from .forms import FeedbackForm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Paragraph, SimpleDocTemplate, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime 

# Create your views here.
@auth
def index(request):

    return render(request,'index.html')

@auth
def webdev(request):

    return render(request,'webdev.html')

@auth
def datascience(request):

    return render(request,'datascience.html')

@auth
def mobiledev(request):

    return render(request,'mobiledev.html')

@auth
def aiml(request):

    return render(request,'aiml.html')

@auth
def cybersec(request):

    return render(request,'cybersec.html')

@auth
def cloudcomp(request):

    return render(request,'cloudcomputing.html')

@auth
def rts(request):

    return render(request,'rts.html')

@auth
def ccl(request):
    
    return render(request,'ccl.html')

@auth
def csqr(request):

    return render(request,'csqr.html')

def status(request):
    return render(request,'thankyou.html')

@unauth
def landing(request):
    return render(request,'landing_page.html')

@unauth
def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        initial_data={'username':'','password1':'','password2':''}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'signup.html', {'form':form})

@unauth
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)  
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin_dashboard')  # Change this to your admin page URL
                else:
                    return redirect('index') 
            
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    else:
        initial_data = {'username': '', 'password': ''}
        form = AuthenticationForm(initial=initial_data)
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')

def feedback_form(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')  # Redirect after successful submission
    else:
        form = FeedbackForm()
    
    return render(request, "feedback.html", {"form": form})


@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")
    
    # Fetch only the required fields
    feedbacks = Feedback.objects.values(
        'student_name',  
        'email',  
        'course_name',  
        'course_rating',  
        'content_relevance',   
        'interface_rating',  
        'best_feature',  
        'additional_feedback', 
    )

    return render(request, 'admin_dashboard.html', {'feedbacks': feedbacks})

from django.http import JsonResponse

from django.http import JsonResponse

# Predefined responses for tech terms and programming languages
PREDEFINED_RESPONSES = {
    # Programming languages
    "python": "Python is a versatile language for web development, data science, AI, and automation.",
    "java": "Java is widely used for enterprise apps, Android development, and backend systems.",
    "c++": "C++ is great for system programming, game development, and performance-critical applications.",
    "c#": "C# is mainly used for Windows apps, Unity games, and backend development with .NET.",
    "javascript": "JavaScript is essential for frontend web development and can also be used on the backend with Node.js.",
    "typescript": "TypeScript is a strongly typed superset of JavaScript for safer, scalable code.",
    "go": "Go (Golang) is efficient for backend services, microservices, and cloud applications.",
    "ruby": "Ruby is known for web development with Ruby on Rails.",
    "php": "PHP is widely used for server-side web development and content management systems.",
    "rust": "Rust focuses on safety and performance, often used in systems programming.",

    # Web development
    "html": "HTML is the standard markup language for creating web pages.",
    "css": "CSS styles HTML content and controls the visual layout of web pages.",
    "django": "Django is a high-level Python web framework that encourages rapid development.",
    "flask": "Flask is a lightweight Python web framework for building web apps quickly.",
    "react": "React is a JavaScript library for building interactive user interfaces.",
    "angular": "Angular is a TypeScript-based framework for building dynamic web applications.",
    "vue": "Vue.js is a progressive JavaScript framework for building user interfaces.",
    "bootstrap": "Bootstrap is a CSS framework for responsive and mobile-first web design.",
    "tailwind": "Tailwind CSS is a utility-first CSS framework for rapid UI development.",

    # Databases
    "mysql": "MySQL is a popular open-source relational database system.",
    "postgresql": "PostgreSQL is an advanced open-source relational database known for reliability.",
    "mongodb": "MongoDB is a NoSQL database that stores data in flexible JSON-like documents.",
    "sqlite": "SQLite is a lightweight, file-based relational database ideal for small apps.",
    "redis": "Redis is an in-memory database used for caching and fast data storage.",

    # Version control & DevOps
    "git": "Git is a version control system that tracks changes in source code.",
    "github": "GitHub is a platform for hosting Git repositories and collaborating on code.",
    "docker": "Docker is a platform for containerizing applications for consistent deployment.",
    "kubernetes": "Kubernetes is used to orchestrate and manage containerized applications.",
    "ci/cd": "CI/CD automates testing and deployment to improve software delivery.",

    # AI/ML
    "ai": "Artificial Intelligence enables machines to mimic human intelligence.",
    "ml": "Machine Learning is a subset of AI where systems learn from data.",
    "deep learning": "Deep Learning uses neural networks to model complex patterns in data.",
    "tensorflow": "TensorFlow is an open-source library for machine learning and deep learning.",
    "pytorch": "PyTorch is a flexible deep learning library used for AI research and production.",

    # Cloud & Hosting
    "aws": "AWS is a cloud platform offering compute, storage, and many other services.",
    "azure": "Azure is Microsoft’s cloud platform for hosting and managing applications.",
    "gcp": "Google Cloud Platform offers cloud computing services including databases and ML tools.",
    "render": "Render is a cloud platform for deploying web apps and services easily.",
    "heroku": "Heroku is a cloud platform for deploying web apps quickly.",

    # Networking & Security
    "http": "HTTP is the protocol used for communication between web servers and clients.",
    "https": "HTTPS is a secure version of HTTP using encryption (TLS/SSL).",
    "api": "An API (Application Programming Interface) allows apps to communicate with each other.",
    "rest": "REST is a standard for building APIs with stateless requests.",
    "graphql": "GraphQL is a flexible API query language for retrieving only the data you need.",
    "jwt": "JWT (JSON Web Token) is used for secure user authentication in web apps.",
    "oauth": "OAuth is a protocol for secure authorization of apps without sharing passwords.",

    # Miscellaneous tech
    "linux": "Linux is an open-source operating system widely used for servers and development.",
    "windows": "Windows is a popular operating system for desktops and servers.",
    "macos": "macOS is Apple’s desktop operating system.",
    "vscode": "VS Code is a lightweight and popular code editor from Microsoft.",
    "intellij": "IntelliJ IDEA is a powerful IDE mainly for Java and Kotlin development.",
    "api key": "API keys are used to authenticate applications accessing APIs.",
    "json": "JSON is a lightweight data format used for exchanging data between applications.",
    "xml": "XML is a markup language used to store and transport data.",
    "oop": "OOP (Object-Oriented Programming) organizes code into objects with data and methods.",
    "restful": "RESTful APIs follow REST principles to provide structured web services.",
}

def chatbot_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('message', '').lower()  # lowercase for matching
        if not user_input:
            return JsonResponse({'error': 'Empty message'}, status=400)
        
        # Check for keywords in user input
        for keyword, response in PREDEFINED_RESPONSES.items():
            if keyword in user_input:
                return JsonResponse({'response': response})
        
        # Default response if no keywords match
        reply = f"You said: {user_input}"
        return JsonResponse({'response': reply})
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def export_feedback_pdf(request):
    if not request.user.is_superuser:
        return HttpResponse("Unauthorized", status=401)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Feedback_Report.pdf"'  # Force download

    doc = SimpleDocTemplate(response, pagesize=letter, topMargin=60, leftMargin=50, rightMargin=50)
    styles = getSampleStyleSheet()
    elements = []

    feedbacks = Feedback.objects.all()
    current_date = datetime.now().strftime("%d-%m-%Y")  # Get current date

    for index, feedback in enumerate(feedbacks):
        # Title centered
        title = Paragraph("<b>UpSkillX - Feedback Report</b>", styles["Title"])
        title_table = Table([[title]], colWidths=[500])  # Full-width table to center title
        title_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 20),
        ]))
        elements.append(title_table)

        # Header with Date (left) and Generated by (right)
        header_data = [
            [Paragraph(f"<b>Date:</b> {current_date}", styles["Normal"]),  
             Paragraph(f"<b>Generated by:</b> {request.user.username}", styles["Normal"])]
        ]
        header_table = Table(header_data, colWidths=[350, 150])  # Equal column widths
        header_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),  # Date aligned left
            ('ALIGN', (0, 1), (0, 1), 'RIGHT'),  # Generated by aligned right
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ]))
        elements.append(header_table)
        elements.append(Spacer(1, 10))  # Space before title

        # Feedback table data
        data = [
            ["Student Name", Paragraph(feedback.student_name, styles["Normal"])],
            ["Email", Paragraph(feedback.email, styles["Normal"])],
            ["Course Name", Paragraph(feedback.course_name, styles["Normal"])],
            ["Course Rating", Paragraph(str(feedback.course_rating), styles["Normal"])],
            ["Content Understandability", Paragraph(feedback.content_understandability, styles["Normal"])],
            ["Content Relevance", Paragraph(feedback.content_relevance, styles["Normal"])],
            ["Content Suggestions", Paragraph(feedback.content_suggestions, styles["Normal"])],
            ["Interface Rating", Paragraph(str(feedback.interface_rating), styles["Normal"])],
            ["Technical Issues", Paragraph(feedback.technical_issues, styles["Normal"])],
            ["Issue Details", Paragraph(feedback.issue_details, styles["Normal"])],
            ["Navigation Ease", Paragraph(feedback.navigation_easy, styles["Normal"])],
            ["Usability Suggestions", Paragraph(feedback.usability_suggestions, styles["Normal"])],
            ["Recommend", Paragraph(feedback.recommend, styles["Normal"])],
            ["Best Features", Paragraph(feedback.best_feature, styles["Normal"])],
            ["Additional Feedback", Paragraph(feedback.additional_feedback, styles["Normal"])]
        ]

        table = Table(data, colWidths=[200, 300])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.lightblue),  # Light blue background
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)

        # Add a page break after each feedback except the last one
        if index < len(feedbacks) - 1:
            elements.append(PageBreak())

    doc.build(elements)
    return response