from django import forms
from myproject.core.models import Video


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = '__all__'