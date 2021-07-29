from django.http.response import HttpResponseRedirect
from .forms import StatusForm
from .models import Job_application, Status,Skill
from os import error
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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

@login_required
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

@login_required
def jobs_detail(request, job_id):
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

#StatusViews
@login_required
def add_status(request, job_id):
    form = StatusForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.job_app_id = job_id
        new_status.save()
    
    return redirect('detail', job_id=job_id)

@login_required
def update_status(request, status_id):
    status = get_object_or_404(Status, id=status_id)

    if request.method != 'POST':
        form = StatusForm(instance=status)

    else:
        form = StatusForm(instance=status, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail', args=[status.job_app.id]))
             
    return render(request, 'status/update.html', {'form': form, 'status': status })

@login_required
def delete_status(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    if request.method == 'POST':
        status.delete()
        return HttpResponseRedirect(reverse('detail', args=[status.job_app.id]))

    return render(request, 'status/delete.html', {'status': status})

#ProfileViews
class SkillList(LoginRequiredMixin, ListView):
  model = Skill

class SkillDetail(LoginRequiredMixin, DetailView):
  model = Skill

class SkillCreate(LoginRequiredMixin, CreateView):
  model = Skill
  fields = ['name','level']
  
  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SkillUpdate(LoginRequiredMixin, UpdateView):
  model = Skill
  fields = ['name','level']
  
class SkillDelete(LoginRequiredMixin, DeleteView):
  model = Skill
  success_url = '/skills/'
