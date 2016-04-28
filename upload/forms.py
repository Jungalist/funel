from django import forms

from .models import Upload

class UploadFileForm(forms.ModelForm):
    email = forms.EmailField(label="Email", max_length=50)
    title = forms.CharField(label="Optional job title", required=False, max_length=50)
    class Meta:
        model = Upload
        fields = ('file', 'setting', 'permutations', 'biohel_runs', 'attributes')






#class LoginForm(forms.Form):
#    username = forms.CharField(label="username", max_length=50)
#    password = 
    
