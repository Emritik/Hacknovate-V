from django.db import models
# Create your models here

class Contact(models.Model):
    name= models.CharField( max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
          return self.email
    

class Appointment(models.Model):
     name = models.CharField(max_length=50)
     email = models.EmailField()
     phone = models.IntegerField()
     chdoc = models.TextField()
     date = models.DateField()
     time = models.TimeField()
     desc = models.TextField()

     def __str__(self):
          return self.email
