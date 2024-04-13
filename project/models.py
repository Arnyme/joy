from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=50,unique=True)
    desription = models.TextField(max_length=255)
    image = models.ImageField(upload_to='project', blank=True, null=True,default='project/noimag.png' )
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    @property
    def gt_image(self):
        if self.image :
            return self.image.url
        return 'project/noimag.png'

    def __str__(self):
        return self.project_name
    


    