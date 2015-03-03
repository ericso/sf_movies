# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.TextField()),
                ('release_year', models.IntegerField(null=True, blank=True)),
                ('locations', models.TextField(null=True, blank=True)),
                ('fun_facts', models.TextField(null=True, blank=True)),
                ('production_company', models.TextField(null=True, blank=True)),
                ('distributor', models.TextField(null=True, blank=True)),
                ('director', models.TextField(null=True, blank=True)),
                ('writer', models.TextField(null=True, blank=True)),
                ('actor_1', models.TextField(null=True, blank=True)),
                ('actor_2', models.TextField(null=True, blank=True)),
                ('actor_3', models.TextField(null=True, blank=True)),
                ('latitude', models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)),
                ('longitude', models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('title', 'locations')]),
        ),
    ]
