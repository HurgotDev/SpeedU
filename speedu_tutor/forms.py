from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo Electrónico', required=True)
    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput)
    rememberme = forms.BooleanField(required=False)

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label='Contraseña actual', required=True, widget=forms.PasswordInput)
    new_password = forms.CharField(label='Nueva contraseña', required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirme la contraseña', required=True, widget=forms.PasswordInput)