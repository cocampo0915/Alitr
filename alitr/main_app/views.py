from .forms import StatusForm
from .models import Job_application, Status,Skill
from os import error
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm# Import the form we just created





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
    jobs = Job_application.objects.filter(user=request.user).order_by('-date')
    statuses = []
    for job in jobs:
        latest_status = Status.objects.filter(job_app=job).first()
        statuses.append(latest_status)
    
    return render(request, 'jobs/index.html', {
        'jobs': jobs, 
        'statuses': statuses,
    })

def jobs_detail(request, job_id):
    job = Job_application.objects.get(id=job_id)
    status_form = StatusForm()
    status = Status.objects.filter(job_app=job_id).first()

    return render(request, 'jobs/detail.html', {
        'job': job,
        'status': status,
        'status_form': status_form,
    })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save() # Save user to Database
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            return redirect('blog-home') # Redirect user to Homepage
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



'''def signup(request):
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
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message })'''

class JobCreate(CreateView):
    model = Job_application
    fields = ['name', 'company', 'location', 'date', 'url', 'requirements', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JobUpdate(UpdateView):
    model = Job_application
    fields = ['name', 'company', 'location', 'date', 'url', 'requirements', 'notes']

class JobDelete(DeleteView):
    model = Job_application
    success_url = '/jobs/'

def add_status(request, job_id):
    form = StatusForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.job_app_id = job_id
        new_status.save()
    
    return redirect('detail', job_id=job_id)

#ProfileViews
class SkillList(ListView):
  model = Skill

class SkillDetail(DetailView):
  model = Skill

class SkillCreate(CreateView):
  model = Skill
  fields = ['name','level']
  
  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SkillUpdate(UpdateView):
  model = Skill
  fields = ['name','level']
  
class SkillDelete(DeleteView):
  model = Skill
  success_url = '/skills/'

# Register Def

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Your account has been created! You are now able to log in') 
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

# Update it here
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.pro) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.pro)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile/update.html', context)