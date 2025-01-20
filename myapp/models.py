from django.db import models

# Create your models here.

class UserRegister(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    mob = models.TextField()
    add = models.TextField()

    
    def __str__(self):
        return self.name