#encoding: utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from Pleby.models import *
from .forms import LoginForm,CreateUsuarioForm, CreateEnqueteForm
from django.contrib.auth.decorators import login_required


def index(request):
	enquetes = Enquete.objects.all()[:3]
	return render(request,"index.html",{'enquetes':enquetes})

def login_user(request):
	form = LoginForm()
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
	return HttpResponseRedirect(reverse('index'))



def detalhe_enquete(request,id):
	enquete = Enquete.objects.get(id=id)
	return render(request,'enquete_detalhe.html',{'enquete':enquete})


def registrar(request):
	if request.user.is_authenticated(): #Se o usuário está autenticado
		return HttpResponseRedirect(reverse("index")) # Redireione
	if request.POST:
		form = CreateUsuarioForm(request.POST) 
		if form.is_valid():
			username 		= form.cleaned_data['username']
			email 			= form.cleaned_data['email']
			password 		= form.cleaned_data['password']
			aniversario 	= form.cleaned_data['aniversario']
			user 			= User.objects.create_user(username=username,password=password,email=email)
			user.is_active  = True
			user.save()
			usuario 		= Usuario(user_auth=user,data_nascimento=aniversario)
			usuario.save()
			user 			= authenticate(username=username,password=password)
			login(request,user)
			return HttpResponseRedirect(reverse("index"))
		return render(request,'registrar.html',{'form':form})
	form = CreateUsuarioForm()
	return render(request,'registrar.html',{'form':form})


@login_required
def create_enquete(request):
	form = CreateEnqueteForm()
	if request.POST:
		form = CreateEnqueteForm(request.POST)
		if form.is_valid():
			titulo 		= form.cleaned_data['titulo']
			descricao 	= form.cleaned_data['descricao']
			tags 		= form.cleaned_data['tags']
			opcoes		= form.cleaned_data['opcoes']
			#Usar Formsets aqui para fazer a lista de perguntas/opções
			# https://stackoverflow.com/questions/17159567/how-to-create-a-list-of-fields-in-django-forms
	return render(request,'create_enquete.html',{'form':form})

@login_required
def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))