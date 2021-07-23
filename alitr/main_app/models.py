from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse #matching url


# Create your models here.
class Job_application(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    date = models.DateField('date applied')
    requirements = models.TextField(max_length=500)
    notes = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'job_id': self.id})#every model instance has its own method 
        #django will now render the detail page, 


class Status(models.Model):
  date = models.DateField('date')
  STATUS = (
      ('1', 'Applied'),
      ('2', 'In Progress'),
      ('3', 'Interview scheduled'),
      ('4', 'Interview complete'),
      ('5', 'Job Offer'),
      ('6', 'Incomplete'),
      ('7', 'Not Selected'),
      ('8', 'Unknown'),

  )
 
  status = models.CharField(
    max_length=1,
    choices=STATUS,
    default=STATUS[0][0]
  )

  job_app = models.ForeignKey(Job_application, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_status_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']