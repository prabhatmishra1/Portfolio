from django.db import models

# Create your models here.

class Contact(models.Model):
    """This class will store the contact details of client"""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name