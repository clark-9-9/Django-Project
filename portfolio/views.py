from django.shortcuts import render

# Create your views here.

def index(request):
    """View for the home page"""
    return render(request, 'portfolio/home.html', {
        'title': 'Home'
    })

def about(request):
    """View for the about page"""
    return render(request, 'portfolio/about.html', {
        'title': 'About Me'
    })

def projects(request):
    """View for the projects page"""
    return render(request, 'portfolio/projects.html', {
        'title': 'Projects'
    })

def contact(request):
    """View for the contact page"""
    return render(request, 'portfolio/contact.html', {
        'title': 'Contact'
    })
