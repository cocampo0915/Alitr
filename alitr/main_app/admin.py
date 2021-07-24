from .models import Attachment, Job_application, Status
from django.contrib import admin

# Register your models here.
admin.site.register(Job_application)
admin.site.register(Status)
admin.site.register(Attachment)
