# Generated by Django 2.2 on 2019-05-02 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0003_shoe_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
