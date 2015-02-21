# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.IntegerField(choices=[(1, 'Pública'), (2, 'Privada')], default=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Colores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('estilo', models.CharField(max_length=300)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=200)),
                ('agenda', models.ForeignKey(to='agenda.Agenda')),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactNetwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=255)),
                ('contact', models.ForeignKey(to='agenda.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Localization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('contact', models.ForeignKey(to='agenda.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='agenda',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, to='agenda.Grupo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agenda',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
