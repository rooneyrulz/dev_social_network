from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
  text = forms.CharField(
    label='Comment',
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter your comment...'
      }
    )
  )

  class Meta:
    model = Comment
    fields = ('text',)

  def clean_text(self, *args, **kwargs):
    text = self.cleaned_data.get('text')
    if not text:
      raise forms.ValidationError('Invalid field!')
    else:
      return text