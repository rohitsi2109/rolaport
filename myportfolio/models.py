from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=125)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    message = models.TextField()
    date = models.DateField()
   
    def __str__(self):
        return self.name