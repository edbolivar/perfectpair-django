# Generated by Django 2.2.1 on 2019-05-11 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0006_shoe_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
