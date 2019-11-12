from django.db import models
from django.conf import settings


GENDER_CHOICES = [
  ('M', 'Male'),
  ('F', 'Female')
]

STATUS_CHOICES = [
  ('M', 'Married'),
  ('S', 'Single')
]

PROFESSION_CHOICES = [
  ('S/L', 'Student or Learning'),
  ('JD', 'Junior Developer'),
  ('SD', 'Senior Developer'),
  ('D', 'Developer'),
  ('M', 'Manager'),
  ('I/T', 'Instructor or Teacher'),
  ('I', 'Intern'),
  ('B', 'Bussiness Man'),
  ('DM', 'Digital Marketer'),
  ('DS', 'Data Scientist'),
  ('O', 'Other')
]


class Profile(models.Model):
  user = models.ForeignKey(
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
