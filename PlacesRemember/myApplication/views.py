from django.shortcuts import render
from django.contrib.auth import authenticate, login

def welcome(request):
    memories = []  # Replace with your actual memory data
    context = {'memories': memories}
    return render(request, 'welcome.html', context)



# Create your views here.
