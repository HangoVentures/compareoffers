# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(default=0, null=True, blank=True)),
                ('sex', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='locationzip',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('visitor_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='offers.Visitor')),
                ('edlevel', models.CharField(default=b'GR', max_length=2, choices=[(b'UG', b'Undergraduate Degree'), (b'GR', b'Masters Degree'), (b'PD', b'Doctors Degree')])),
            ],
            bases=('offers.visitor',),
        ),
    ]
