from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Job Apps
    path('jobs/', views.jobs_index, name='index'),
    path('jobs/<int:job_id>', views.jobs_detail, name='detail'),
    # Company

    # User
    path('accounts/signup', views.signup, name='signup'),
]