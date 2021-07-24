# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse #matching url

# Create your models here.
class Job_application(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    date = models.DateField('Date Applied')
    url = models.CharField(
        max_length=250,
        blank=True
        )
    requirements = models.TextField(
        max_length=500,
        blank=True
        )
    notes = models.TextField(
        max_length=500,
        blank=True
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'job_id': self.id}) #every model instance has its own method 
        #django will now render the detail page, 

class Attachment(models.Model): # will implement later with AWS if possible -CO
    url = models.CharField(max_length=250)
    job_app = models.ForeignKey(Job_application, on_delete=models.CASCADE)

    def __str__(self):
        return f'Attachment for job_id: {self.job_id} @{self.url}'

class Status(models.Model):
  date = models.DateField('Date')

  STATUS = (
        ('A', 'Applied'),
        ('B', 'In Progress'),
        ('C', 'Interview scheduled'),
        ('D', 'Interview complete'),
        ('E', 'Job Offer'),
        ('F', 'Incomplete'),
        ('G', 'Not Selected'),
        ('H', 'Unknown'),
  )
 
  status = models.CharField(
    max_length=1,
    choices=STATUS,
    default=STATUS[0][0]
  )

  job_app = models.ForeignKey(Job_application, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_status_display()}"

  # change the default sort
  class Meta:
    ordering = ['-date']

# placeholder for Company model if possible -CO

#User Profile model 
class Profile(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  experience = models.TextField(max_length=500,
        blank=True)
  goals = models.TextField(max_length=500,
        blank=True)


  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('profiles_detail', kwargs={'pk': self.id})