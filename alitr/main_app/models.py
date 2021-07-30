# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse #matching url
from PIL import Image

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
class Skill(models.Model):

  SKILL = (
    ('1','Level 1'),
    ('2','Level 2'),
    ('3','Level 3'),
    ('4','Level 4'),
    ('5','Level 5'),
  )


  
  name = models.CharField(
    max_length=100,
    blank=True
  )
  level = models.CharField(
    max_length=1,
    choices=SKILL,
    default=SKILL[0][0]
  )


  

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('skills_detail', kwargs={'pk': self.id})

#Profile Model 
class Pro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Pro' #show how we want it to be displayed
    class Meta:
        verbose_name_plural = "pro"
    # Override the save method of the model
    def save(self, *args, **kwargs):
        super(Pro, self).save(*args, **kwargs)

        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image
