#encoding: utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

from Pleby.models import *
from .forms import LoginForm,CreateUsuarioForm, CreateEnqueteForm, OpcaoFormSet


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



def detail_enquete(request,id):
	enquete = Enquete.objects.get(id=id)
	opcoes = Opcao.objects.filter(enquete=enquete)
	return render(request,'detail_enquete.html',{'enquete':enquete,'opcoes':opcoes})


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
	formset = OpcaoFormSet()
	if request.POST:
		form 	= CreateEnqueteForm(request.POST)
		formset = OpcaoFormSet(request.POST)
		if form.is_valid() and formset.is_valid():

			titulo 		= form.cleaned_data['titulo']
			descricao 	= form.cleaned_data['descricao']
			tags_names 	= form.cleaned_data['tags']
			
			tags_names_list	= tags_names.split()
			
			enquete = Enquete(titulo=titulo,descricao=descricao)
			enquete.save()
			
			for title in tags_names_list:
				tag,created = Tag.objects.get_or_create(titulo=title)
				enquete.tags.add(tag)
				tag.save()

			for forms in formset:
				opcao = Opcao(titulo=forms.cleaned_data['titulo'],enquete=enquete)
				opcao.save()
			return HttpResponseRedirect(reverse("index"))
			# nova_enquete = Enquete(titulo=titulo,descricao=descricao)
			#Usar Formsets aqui para fazer a lista de perguntas/opções
			# https://stackoverflow.com/questions/17159567/how-to-create-a-list-of-fields-in-django-forms
			# https://stackoverflow.com/questions/10817286/django-formset-as-form-field
	return render(request,'create_enquete.html',{'form':form,'formset':formset})

def list_enquetes_by_tag(request,titulo):
	tag = Tag.objects.get(titulo=titulo) #TODO: Aqui tá pegando pelo ID. melhor seria pelo título. Pesquisar
	if tag:
		enquetes = Enquete.objects.filter(tags=tag)
	else:
		raise Http404
	return render(request,'list_enquetes_by_tag.html',{'enquetes':enquetes})

@login_required
def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))