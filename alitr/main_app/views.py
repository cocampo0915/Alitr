from .forms import StatusForm
from .models import Job_application, Status
from os import error
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Profile



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
    jobs = Job_application.objects.filter(user=request.user).order_by('-date')
    return render(request, 'jobs/index.html', {'jobs': jobs})

def jobs_detail(request, job_id):
    # insert jobs model here
    job = Job_application.objects.get(id=job_id)
    status_form = StatusForm()
    status = Status.objects.filter(job_app=job_id).first()

    return render(request, 'jobs/detail.html', {
        'job': job,
        'status': status,
        'status_form': status_form,
    })

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

class JobCreate(LoginRequiredMixin, CreateView):
    model = Job_application
    fields = ['name', 'company', 'location', 'date', 'url', 'requirements', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job_application
    fields = ['name', 'company', 'location', 'date', 'url', 'requirements', 'notes']

class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job_application
    success_url = '/jobs/'

def add_status(request, job_id):
    form = StatusForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.job_id = job_id
        new_status.save()
    
    return redirect('detail', job_id=job_id)

#ProfileViews
class ProfileList(ListView):
  model = Profile

class ProfileDetail(DetailView):
  model = Profile

class ProfileCreate(CreateView):
  model = Profile
  fields = '__all__'

class ProfileUpdate(UpdateView):
  model = Profile
  fields = ['name', 'email']

class ProfileDelete(DeleteView):
  model = Profile
  success_url = '/profiles/'
