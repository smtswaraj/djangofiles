from django.db import models

# Create your models here.
class upload(models.Model):
    file_Upload = models.ImageField(upload_to = "image")


    def __str__(self):
            return f'file is :- {self.file_Upload}'