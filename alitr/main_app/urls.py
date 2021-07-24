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
    path('accounts/signup', views.signup, name='signup'),
    #Profile
    path('profiles/', views.ProfileList.as_view(), name='profiles_index'),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name='profiles_detail'),
    path('profiles/create/', views.ProfileCreate.as_view(), name='profiles_create'),
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('profiles/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profiles_delete'),
    
]

urlpatterns += staticfiles_urlpatterns()