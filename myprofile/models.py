from django.db import models
from django.contrib.auth import get_user_model, get_user
# Create your models here.
freelancing_choices=(('available', 'Available'), ('busy', 'Busy'))
class Profile(models.Model):

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True)
    phone_number = models.IntegerField()
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField()
    title = models.CharField(max_length=100, blank=True, null=True)
    currently_working = models.BooleanField(default=False)
    freelancing = models.CharField(max_length=50, choices=freelancing_choices, default='available')
    photo = models.ImageField(upload_to='image/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    @property
    def get_full_name(self):
        return self.first_name + '' + self.last_name
    def natural_key(self):
        return self.first_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name    
class PersonalSkill(models.Model):
    skill_name= models.CharField(max_length=80)
    skill_description= models.TextField()
    years_experience = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='personal_skills')
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.skill_name
level_choices = (('newbie', 'Newbie'), ('intermediate', 'Intermediate'), ('professional', 'Professional'), ('expert', 'Expert'))
class TechnicalSkill(models.Model):
    skill_name= models.CharField(max_length=80)
    skill_description= models.TextField()
    skill_level = models.CharField(max_length=30, choices=level_choices,default='--------') 
    years_experience = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='technical_skills')
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.skill_name  
class Course(models.Model):
    course_name = models.CharField(max_length=80)
    course_institute_name = models.CharField(max_length=80)
    duration = models.DurationField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='courses')
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.course_name 
class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    current_work = models.BooleanField(default=False)
    experience_description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name 
class Language(models.Model):
    language_name = models.CharField(max_length=80)
    language_level = models.CharField(max_length=80)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='languages')
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.language_name 



class Blog(models.Model):
    blog_name = models.CharField(max_length=120)
    description = models.TextField()
    images = models.ImageField(upload_to="blog_image/")
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='blogs')
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        self.blog_name

class ProfileAccount(models.Model):
    account_name = models.CharField(max_length=80)
    link = models.URLField()
    additional_info = models.TextField(null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_accounts')
    def __str__(self):
        return self.account_name

class FreelancingAccount(models.Model):
    freelancing_name = models.CharField(max_length=80)
    link = models.URLField()
    additional_info = models.TextField(null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='freelancing_accounts')
    def __str__(self):
        return self.freelancing_name 


