from django.db import models

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=50,unique=True)
    qoute = models.TextField(max_length=255)
    image =models.FileField( upload_to='client/', max_length=100)
    def __str__(self):
        return self.client_name