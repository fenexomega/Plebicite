from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from Pleby.models import *
from .forms import LoginForm,CreateUsuarioForm

def index(request):
	enquetes = Enquete.objects.all()[:3]
	return render(request,"index.html",{'enquetes':enquetes})

def login_user(request):
	if request.POST:
		form = LoginForm(request.POST) 
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user 	 = authenticate(username=username,password=password)
			if user:
				login(request,user)
				if request.GET.get('next') is not None:
					return redirect(request.GET['next'])
			else:
				return HttpResponseRedirect(reverse('index'))
	form = LoginForm()
	return HttpResponseRedirect(reverse('index'))



def detalhe_enquete(request,id):
	enquete = Enquete.objects.get(id=id)
	return render(request,'enquete_detalhe.html',{'enquete':enquete})


def create_usuario(request):
	if request.POST:
		form = CreateUsuarioForm(request.POST) 
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = User.objects.create_user(username=username,password=password,email=email)
			user.is_active = True
			user.save()
			usuario = Usuario(user_auth=user,)
		return render(request,'create_usuario.html',{'form':form})
	form = CreateUsuarioForm()
	return render(request,'create_usuario.html',{'form':form})

def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))