from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    # class Meta:
    #     model = Product
    #     fields = ("title", "price", "description", "featured")

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    

    def clean_username(self):
    	username = self.cleaned_data.get('username')
    	qs = User.objects.filter(username=username)
    	if qs.exists():
    		raise forms.ValidationError("Username needs to be Unique")
    	return username

    def clean(self):
    	data = self.cleaned_data
    	password = data.get('password')
    	password2 = data.get('password2')
    	if password2 != password:
    		raise forms.ValidationError("Passwords must match")
    	return data