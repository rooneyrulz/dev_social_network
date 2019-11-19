from django import forms
from .models import Profile, Education, Experience, Social


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


class ProfileForm(forms.ModelForm):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Name'
      }
    )
  )

  age = forms.IntegerField(
    widget=forms.NumberInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Age'
      }
    )
  )

  gender = forms.ChoiceField(
    choices=GENDER_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  status = forms.ChoiceField(
    choices=STATUS_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  website = forms.CharField(
    required=False,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Website'
      }
    )
  )

  company = forms.CharField(
    required=False,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Company'
      }
    )
  )

  profession = forms.ChoiceField(
    choices=PROFESSION_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  
  location = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Country'
      }
    )
  )

  skills = forms.CharField(
    required=False,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Skills'
      }
    )
  )

  bio = forms.CharField(
    widget=forms.Textarea(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Country',
        'rows': 4
      }
    )
  )

  image = forms.ImageField(
    required=False,
    widget=forms.FileInput(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  class Meta:
    model = Profile
    fields = ('name', 'age', 'gender', 'status', 'website', 'company', 'profession', 'location', 'skills', 'bio', 'image',)

  def clean_age(self, *args, **kwargs):
    age = self.cleaned_data.get('age')
    if age > 50:
      raise forms.ValidationError('Age must be belove 50 years!')
    elif age < 18:
      raise forms.ValidationError('Age must be at least 18 years!')
    else:
      return age


class EducationForm(forms.ModelForm):
  college = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter College'
      }
    )
  )

  degree = forms.ChoiceField(
    choices=DEGREE_CHOICES,
    widget=forms.Select(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  started_at = forms.DateField(
    widget=forms.DateInput(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  ended_at = forms.DateField(
    widget=forms.DateInput(
      attrs={
        'class': 'form-control form-control-lg',
      }
    )
  )

  is_currently_studying = forms.BooleanField(
    label='currently studying',
    widget=forms.CheckboxInput(
      attrs={
        'class': '',
      }
    )
  )
  class Meta:
    model = Education
    fields = ('college', 'degree', 'started_at', 'ended_at', 'is_currently_studying',)


class ExperienceForm(forms.ModelForm):
  class Meta:
    model = Experience
    fields = ('company', 'profession', 'started_at', 'ended_at', 'is_currently_working',)
