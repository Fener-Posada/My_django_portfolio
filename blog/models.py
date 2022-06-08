from django.db import models
import datetime 

# Create your models here.
class Posts(models.Model):
    Title = models.CharField(max_length= 100)
    Description = models.TextField()
    Image = models.ImageField(upload_to = "blog/images")
    Date = models.DateField(datetime.date.today)