from django import forms

from service.models import Feedback


class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

