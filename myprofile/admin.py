from django.contrib import admin
from .models import Profile, Course, Experience, Language, PersonalSkill, TechnicalSkill, ProfileAccount, FreelancingAccount
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(PersonalSkill)
class PersonalSkillAdmin(admin.ModelAdmin):
    pass

@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileAccount)
class ProfileAccountAdmin(admin.ModelAdmin):
    pass