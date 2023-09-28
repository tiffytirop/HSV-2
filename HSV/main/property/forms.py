from django import forms
from property.models import ImageModel

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']