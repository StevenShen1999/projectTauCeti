from django.db import models

# Create your models here.

class Note(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=255)

    points = models.FloatField(default=0)
    price = models.FloatField(default=0)

    upload_time = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255, default=None)

    # Foreign Keys
    # courseID 
    # uploaderID