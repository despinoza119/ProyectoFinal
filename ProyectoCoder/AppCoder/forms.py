from django import forms
from django.contrib.auth.forms import UserCreationForm,User

class BasketFormulario(forms.Form):

    nombre_equipo=forms.CharField()
    entrenador = forms.CharField(max_length=40)
    fundacion = forms.DateField()
    apodo = forms.CharField(max_length=40)
    ubicacion = forms.CharField(max_length=40)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir la contraseña',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar E-mail")
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir la contraseña',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['email','password1','password2']
        help_texts={k:"" for k in fields}