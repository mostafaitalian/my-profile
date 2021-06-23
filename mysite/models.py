from django.db import models
from myprofile.models import Profile

# Create your models here.
class MySite(models.Model):
    project_name = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField()
    images = models.ImageField(upload_to='image/')
    myprofile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sites")
    def __str__(self):
        return self.project_name