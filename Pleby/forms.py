# encoding: utf-8
from django import forms
from django.contrib.auth import authenticate
import datetime
from django.forms import extras
from Pleby.models import Enquete

def getYear():
	return (datetime.datetime.utcnow() - datetime.timedelta(hours=11)).year

class LoginForm(forms.Form):
	username = forms.CharField(label="Login",max_length=30,widget=forms.TextInput(attrs={'placeholder':'Login','class':'form-control'}))
	password = forms.CharField(label="Senha",max_length=30,widget=forms.PasswordInput(attrs={'placeholder':'Senha','class':'form-control'}))
	def clean(self):
		cleaned_data = super(LoginForm,self).clean()
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if not authenticate(username=username,password=password):
			raise forms.ValidationError("Login ou senha incorretos!")
		return self.cleaned_data

class CreateUsuarioForm(forms.Form):
	username 		  = forms.CharField(label="Login",max_length=30,widget=forms.TextInput(attrs={'placeholder':'Login','class':'input-block-level'}))
	password 		  = forms.CharField(label="Senha",max_length=30,widget=forms.PasswordInput(attrs={'placeholder':'Senha','class':'input-block-level'}))
	password_confirm  = forms.CharField(label="Repita a Senha",max_length=30,widget=forms.PasswordInput(attrs={'placeholder':'Confirmação','class':'input-block-level'}))
	email 			  = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder':'Email','class':'input-block-level'}))
	email_confimation = forms.EmailField(label="Confirmação de Email",widget=forms.TextInput(attrs={'placeholder':'Confirmação','class':'input-block-level'}))
	aniversario 	  = forms.DateField(widget=extras.SelectDateWidget())
	def clean(self):
		cleaned_data  = super(CreateUsuarioForm,self).clean()
		password = cleaned_data.get('password',None)
		password_confirm = cleaned_data.get('password_confirm',None)
		email = cleaned_data.get('email',None)
		email_confirm = cleaned_data.get('email_confimation',None)
		if email_confirm != email:
			raise forms.ValidationError("Os emails não conferem!")
		if password_confirm != password:
			raise forms.ValidationError("As senhas não conferem!")
		return self.cleaned_data

class CreateEnqueteForm(forms.ModelForm):
	class Meta:
		model = Enquete
		exclude = []