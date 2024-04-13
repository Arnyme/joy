from django.db import models
from django.utils.timezone import datetime
# Create your models here.
class Member(models.Model):
    gender =[
        ('male','male'),
        ('female','female'),
    ]
    active =[
        ('active','true'),
        ('unactive','false'),
    ]

    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.CharField( max_length=255,unique=True)
    sex = models.CharField(max_length=10, choices=gender)
    password = models.CharField(max_length=50,null=True)
    profile_pic =models.ImageField( upload_to='member/', height_field=None, width_field=None, max_length=None,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    is_active = models.BooleanField(default=True,choices=active)

    class Meta:
        
        verbose_name = "member"
        verbose_name_plural = "members"

    def __str__(self):
        return self.first_name
