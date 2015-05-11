from django import forms
from django.contrib.auth.models import User
# # from authentication.models import User
from iq_app.models import Registration

class UserForm(forms.ModelForm):
	firstname = forms.CharField(max_length=32, required=True, help_text="firstname")
	username = forms.CharField(max_length=32, required=True, help_text="username")
	email = forms.EmailField(max_length=32, required=True, help_text="email")
	password = forms.CharField(required=True, widget=forms.PasswordInput(), help_text="password")
	# age = forms.CharField(max_length=5, required=True, help_text="age")


	class Meta:
		model = User
		fields = ('firstname', 'username', 'email', 'password')

class RegistrationForm(forms.ModelForm):
	age = forms.CharField(max_length=5, required=True, help_text="age")
	class Meta:
		model = Registration
		fields = ('age',)


	# def save(self, commit=True):
	# 	user = super(UserForm, self).save(commit=False)
	# 	user.set_password(self.cleaned_data["password"])
	# 	if commit:
	# 		user.save()
	# 	return user


