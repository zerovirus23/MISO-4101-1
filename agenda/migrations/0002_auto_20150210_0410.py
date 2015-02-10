# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
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
            name='type',
            field=models.IntegerField(choices=[(1, 'Pública'), (2, 'Privada')], default=2),
            preserve_default=True,
        ),
    ]
