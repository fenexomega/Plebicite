# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

class Tag(models.Model):
	titulo 				= models.CharField(max_length=150,blank=None,unique=True)
	def __unicode__(self):
		return self.titulo

class Opcao(models.Model):
	titulo 				= models.CharField(max_length=100,blank=None)
	votos 				= models.IntegerField(default=0)
	enquete 			= models.ForeignKey('Enquete')
	def __unicode__(self):
		return self.titulo

class Enquete(models.Model):
	titulo 				= models.CharField(max_length=500,blank=None)
	descricao 			= models.TextField(blank=None)
	tags 				= models.ManyToManyField(Tag,blank=None)
	data_ultima_votacao = models.DateField(null=True,blank=None)
	data_validade 		= models.DateField(null=False,blank=None,default=datetime.now() + timedelta(days=7))
	data_criacao		= models.DateField(auto_now_add=True)
	def __unicode__(self):
		return self.titulo

class Usuario(models.Model):
	user_auth 			= models.OneToOneField(User,primary_key=True)
	data_nascimento 	= models.DateField(verbose_name="Data de Nascimento",null=False,blank=False)
	data_criado 		= models.DateTimeField(verbose_name="Data de Cadastro",auto_now_add=True)
	enquetes_votadas	= models.ManyToManyField(Enquete,through="RelacaoUsuarioEnquete")
	especial 			= models.BooleanField(default=False)
	def __unicode__(self):
		return self.user_auth.username

class RelacaoUsuarioEnquete(models.Model):
	usuario 			= models.ForeignKey(Usuario)
	enquete 			= models.ForeignKey(Enquete)
	hora_e_data 		= models.DateTimeField(auto_now_add=True)
