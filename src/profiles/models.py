from django.db import models
from django.conf import settings


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
  pass


# EXPERIENCES MODEL
class Experience(models.Model):
  pass


# SOCIAL MODEL
class Social(models.Model):
  pass
