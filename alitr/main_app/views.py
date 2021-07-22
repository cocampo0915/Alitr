from os import error
from django.shortcuts import render, redirect

# imports for user authentication
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def jobs_index(request):
    # insert jobs model here

    return render(request, 'jobs/index.html')

def jobs_detail(request, job_id):
    # insert jobs model here
    return render(request, 'jobs/detail.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid signup data - please try again'
    
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message })