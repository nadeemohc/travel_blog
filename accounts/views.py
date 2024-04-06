# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def signup(request):
    context = {
        'form': form,
        'title':'Signup',
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:home')
    else:
        form = UserCreationForm()
    return render(request, 'templates/signup.html', context)

def login_view(request):
    context = {
        'title':'Login',
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:home')
        else:
            messages.error(request, "")
    return render(request, 'templates/login.html', context)