from django.db import models
from myprofile.models import Profile
# Create your models here.


class Project(models.Model):
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects', default=1)
    title = models.CharField(max_length=80)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='media/img/')
    url = models.URLField()

    def __str__(self):
        return self.title 