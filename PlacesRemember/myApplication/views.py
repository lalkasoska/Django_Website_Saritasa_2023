from django.shortcuts import render
from django.contrib.auth import authenticate, login

def home(request):
    memories = []  # Replace with your actual memory data
    context = {'memories': memories}
    return render(request, 'home.html', context)

def login(request):
    # Render the login template
    return render(request, 'login.html')

# Create your views here.
