# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_auto_20151025_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='tuitionbonus',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
