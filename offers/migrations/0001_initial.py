# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('offertype', models.CharField(default=b'NJ', max_length=2, choices=[(b'CJ', b'Current Job'), (b'NJ', b'New Job')])),
                ('companyname', models.CharField(max_length=100, null=True, verbose_name=b'company name', blank=True)),
                ('positionname', models.CharField(max_length=100, null=True, verbose_name=b'position name', blank=True)),
                ('startdate', models.DateField(verbose_name=b'start date')),
                ('annualbase', models.IntegerField()),
                ('annualbonus', models.IntegerField()),
                ('signingbonus', models.IntegerField(default=0, null=True, blank=True)),
                ('stockbonus', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('otherbonus', models.IntegerField(default=0, null=True, blank=True)),
                ('bonusdate', models.DateField(null=True, verbose_name=b'other bonus date', blank=True)),
                ('offer', models.ForeignKey(to='offers.Offer')),
            ],
        ),
        migrations.CreateModel(
            name='Vest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vestingamount', models.IntegerField(default=0, null=True, blank=True)),
                ('vestingdate', models.DateField(null=True, verbose_name=b'vest date', blank=True)),
                ('offer', models.ForeignKey(to='offers.Offer')),
            ],
        ),
    ]
