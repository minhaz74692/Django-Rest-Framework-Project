from django.db import models

# Create your models here.
class Users(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=40, default="")
    phone = models.CharField(max_length=11, default="")

    # def __str__(self):
    #     return {'name': self.name, "email":self.email}
    
    class Meta: 
        ordering = ["created"]
