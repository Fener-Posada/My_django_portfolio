from django.db import models
from django.db.models.fields import CharField,URLField
from django.db.models.fields.files import ImageField
from django.core.validators import FileExtensionValidator
import datetime
class projects(models.Model):
    Title = CharField(max_length= 100)
    Short_Description = CharField(max_length= 200)
    Description = CharField(max_length= 450)
    Image_1 = ImageField(upload_to= 'portfolio/images')
    Image_2 = ImageField(upload_to= 'portfolio/images', blank=True)
    video = models.FileField(upload_to='portfolio/images', blank=True , validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    Url = URLField(blank= True)
    Categoria = CharField(max_length= 250)
    Date = models.DateField(datetime.date.today) 
