from .models import Attachment, Job_application, Status, Skill, Pro, Photo
from django.contrib import admin

# Register your models here.
admin.site.register(Job_application)
admin.site.register(Status)
admin.site.register(Attachment)
admin.site.register(Skill)
admin.site.register(Pro)
admin.site.register(Photo)
