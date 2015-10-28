# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_auto_20151025_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='visitor_ptr',
        ),
        migrations.AddField(
            model_name='offer',
            name='discountrate',
            field=models.FloatField(default=0.08),
        ),
        migrations.AddField(
            model_name='offer',
            name='salarygrowth',
            field=models.FloatField(default=0.15),
        ),
        migrations.AddField(
            model_name='offer',
            name='stockgrowth',
            field=models.FloatField(default=0.1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='annualbonus',
            field=models.FloatField(default=0.1),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Visitor',
        ),
    ]
