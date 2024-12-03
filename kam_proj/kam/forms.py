from django import forms
from .models import Rev


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Rev
        fields = ['user', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
