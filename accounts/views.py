from django.shortcuts import render

# Create your views here.

def perform_login(request):
    return render(request, 'templates/login.html')

def perform_signup(request):
    return render(request, 'templates/signup.html')