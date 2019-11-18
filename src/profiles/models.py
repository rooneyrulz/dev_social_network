from django.db import models
from django.conf import settings
from datetime import datetime


GENDER_CHOICES = [
  ('Male', 'Male'),
  ('Female', 'Female')
]

STATUS_CHOICES = [
  ('Married', 'Married'),
  ('Single', 'Single')
]

PROFESSION_CHOICES = [
  ('Student or Learning', 'Student or Learning'),
  ('Junior Developer', 'Junior Developer'),
  ('Senior Developer', 'Senior Developer'),
  ('Developer', 'Developer'),
  ('Manager', 'Manager'),
  ('Instructor or Teacher', 'Instructor or Teacher'),
  ('Intern', 'Intern'),
  ('ussiness Man', 'Bussiness Man'),
  ('Digital Marketer', 'Digital Marketer'),
  ('Data Scientist', 'Data Scientist'),
  ('Other', 'Other')
]

DEGREE_CHOICES = [
  ('IT', 'Information Technologies'),
  ('Bussiness Managment', 'Bussiness Managment'),
  ('Digital Marketing', 'Digital Marketing'),
  ('Computer Science', 'Computer Science'),
  ('Civil Engineering', 'Civil Engineering'),
  ('AI', 'Artificial & Inteligence'),
  ('Other', 'Other')
]


class Profile(models.Model):
  user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    default=1,
    on_delete=models.CASCADE
  )
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  gender = models.CharField(
    max_length=5,
    default=1,
    choices=GENDER_CHOICES
  )
  status = models.CharField(
    max_length=10,
    default=1,
    choices=STATUS_CHOICES
  )
  website = models.URLField(max_length=283, blank=True, null=True)
  company = models.CharField(max_length=120)
  profession = models.CharField(
    max_length=120,
    default='Web Developer',
    choices=PROFESSION_CHOICES
  )
  location = models.CharField(max_length=100, default='USA')
  skills = models.CharField(max_length=120, choices=None)
  bio = models.TextField(blank=True, default='Hello buddies..!')
  image = models.ImageField(
    upload_to='profiles/',
    default='default.jpg',
    blank=True
  )
  created_at = models.DateTimeField(auto_now_add=True)


  def __str__(self, *args, **kwargs):
    return self.name


# EDUCATION MODEL
class Education(models.Model):
  profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
  college = models.CharField(max_length=120, default='Info Tech', null=True)
  degree = models.CharField(
    max_length=120,
    default=1,
    choices=DEGREE_CHOICES
  )
  started_at = models.DateField(default=datetime.now, null=True)
  ended_at = models.DateField(default=datetime.now, null=True)
  is_currently_studying = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add=True, null=True)


# EXPERIENCES MODEL
class Experience(models.Model):
  profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
  company = models.CharField(max_length=120, default='IFS', null=True)
  profession = models.CharField(
    max_length=120,
    default=1,
    choices=PROFESSION_CHOICES
  )
  started_at = models.DateField(default=datetime.now, null=True)
  ended_at = models.DateField(default=datetime.now, null=True)
  is_currently_working = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)


# SOCIAL MODEL
class Social(models.Model):
  profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
  facebook = models.URLField(max_length=283, blank=True, null=True)
  youtube = models.URLField(max_length=283, blank=True, null=True)
  twitter = models.URLField(max_length=283, blank=True, null=True)
  instagram = models.URLField(max_length=283, blank=True, null=True)
  linkedin = models.URLField(max_length=283, blank=True, null=True)
  github = models.URLField(max_length=283, blank=True, null=True)
  google_plus = models.URLField(max_length=283, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
