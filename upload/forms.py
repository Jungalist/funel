from django import forms

from .models import Upload

class UploadFileForm(forms.ModelForm):

    class Meta:
        model = Upload
<<<<<<< HEAD
        fields = ('title', 'file', 'setting', 'permutations', 'biohel_runs', 'attributes')
=======
        fields = ('title', 'file', 'setting', 'permutations', 'biohel_runs', 'attributes') 
>>>>>>> 4acbc3c4e78a72514afc4810af365620b7142604

#class LoginForm(forms.Form):
#    username = forms.CharField(label="username", max_length=50)
#    password = 
    
