from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Job Apps
    path('jobs/', views.jobs_index, name='index'),
    path('jobs/<int:job_id>/', views.jobs_detail, name='detail'),
    path('jobs/create/', views.JobCreate.as_view(), name='jobs_create'),
    path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='jobs_update'),
    path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='jobs_delete'),
    # Status
    path('jobs/<int:job_id>/add_status/', views.add_status, name='add_status'),
    # Company

    # User
    path('accounts/signup', views.signup, name='signup'),
]