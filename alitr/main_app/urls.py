from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



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
    #path('accounts/signup', views.signup, name='signup'),
    path('accounts/signup', views.signup, name='signup'),
    #Profile 

    path('profile/',views.profile, name='profile'),



    #Skills
    path('skills/', views.SkillList.as_view(), name='skills_index'),
    path('skills/<int:pk>/', views.SkillDetail.as_view(), name='skills_detail'),
    path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
    path('skills/<int:pk>/update/', views.SkillUpdate.as_view(), name='skills_update'),
    path('skills/<int:pk>/delete/', views.SkillDelete.as_view(), name='skills_delete'),



    
]

urlpatterns += staticfiles_urlpatterns()