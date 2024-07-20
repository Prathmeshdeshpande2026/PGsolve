from django.db import models

# Create your models here.

class registration_table(models.Model):
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    email=models.EmailField(max_length=30)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=100)
    zip=models.IntegerField(max_length=10)

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class login_table(models.Model):
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.email}"
