from django import forms

from .models import Upload

class UploadFileForm(forms.ModelForm):

    class Meta:
        model = Upload
        fields = ('title', 'file', 'setting', 'permutations', 'biohel_runs', 'attributes')


#class LoginForm(forms.Form):
#    username = forms.CharField(label="username", max_length=50)
#    password = 
    
