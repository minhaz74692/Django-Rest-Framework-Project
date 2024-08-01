from django.db import models

# Create your models here.
class Users(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=30)

    class Meta: 
        ordering = ["created"]
