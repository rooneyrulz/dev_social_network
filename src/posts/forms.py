from django import forms
from .models import Post


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'description',)

  def clean_title(self, *args, **kwargs):
    title = self.cleaned_data.get('title')
    if not title.strip():
      raise forms.ValidationError('Invalid title!')
    else:
      return title

  def clean_description(self, *args, **kwargs):
    description = self.cleaned_data.get('description')
    if not description.strip():
      raise forms.ValidationError('Invalid description!')
    else:
      return description
