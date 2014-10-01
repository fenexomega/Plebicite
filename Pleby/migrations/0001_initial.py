# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500, blank=None)),
                ('descricao', models.TextField(blank=None)),
                ('data_ultima_votacao', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, blank=None)),
                ('votos', models.IntegerField(default=0)),
                ('enquete', models.ForeignKey(to='Pleby.Enquete')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelacaoUsuarioEnquete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_e_data', models.DateTimeField(auto_now_add=True)),
                ('enquete', models.ForeignKey(to='Pleby.Enquete')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(unique=True, max_length=150, blank=None)),
                ('enquetes', models.ManyToManyField(to='Pleby.Enquete', verbose_name=b'enquetes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_auth', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('data_nascimento', models.DateField(verbose_name=b'Data de Nascimento')),
                ('data_criado', models.DateTimeField(auto_now_add=True, verbose_name=b'Data de Cadastro')),
                ('especial', models.BooleanField(default=False)),
                ('enquetes_votadas', models.ManyToManyField(to='Pleby.Enquete', through='Pleby.RelacaoUsuarioEnquete')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='relacaousuarioenquete',
            name='usuario',
            field=models.ForeignKey(to='Pleby.Usuario'),
            preserve_default=True,
        ),
    ]
