from django.db import models
from django.db.models.fields import CharField,URLField
from django.db.models.fields.files import ImageField
from django.core.validators import FileExtensionValidator

class projects(models.Model):
    Title = CharField(max_length= 100)
    Description = CharField(max_length= 250)
    Image = ImageField(upload_to= 'portfolio/images')
    video = models.FileField(upload_to='portfolio/images',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    Url = URLField(blank= True)
    Categoria = CharField(max_length= 250)

