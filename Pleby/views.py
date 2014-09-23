from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from Pleby.models import *
from .forms import *


def index(request):
	enquetes = Enquete.objects.all()[:3]
	return render(request,"index.html",{'enquetes':enquetes})

def login(request):
	if request.POST:
		form = LoginForm(request.POST) 
		return render(request,'login.html',{'form':form})
	form = LoginForm()
	return render(request,'login.html',{'form':form})

def detalhe_enquete(request,id):
	enquete = Enquete.objects.get(id=id)
	return render(request,'enquete_detalhe.html',{'enquete':enquete})


def create_usuario(request):
	if request.POST:
		form = CreateUsuarioForm(request.POST) 
		return render(request,'create_usuario.html',{'form':form})
	form = CreateUsuarioForm()
	return render(request,'create_usuario.html',{'form':form})

def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))