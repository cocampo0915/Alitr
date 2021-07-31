from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path('status/<int:status_id>/update/', views.update_status, name='update_status'),
    path('status/<int:status_id>/delete/', views.delete_status, name='delete_status'),
    # Company

    # User
    path('accounts/signup', views.signup, name='signup'),
    #Profile 
    path('profile/update',views.profile_update, name='profile_update'),
    path('profile/',views.profile, name='profile'),
    path('profile/<int:pro_id>/add_photo/', views.add_photo, name='add_photo'),

    #Skills
    path('skills/', views.SkillList.as_view(), name='skills_index'),
    path('skills/<int:pk>/', views.SkillDetail.as_view(), name='skills_detail'),
    path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
    path('skills/<int:pk>/update/', views.SkillUpdate.as_view(), name='skills_update'),
    path('skills/<int:pk>/delete/', views.SkillDelete.as_view(), name='skills_delete'),



    
]

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)