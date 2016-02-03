from django import forms

<<<<<<< HEAD
from .models import Upload

class UploadFileForm(forms.ModelForm):

    class Meta:
        model = Upload
        fields = ('title', 'file',)
=======
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
>>>>>>> aceb2a88bdf537939ac483aec46550bdaa9bd2dc
