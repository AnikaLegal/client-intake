# Generated by Django 3.1.7 on 2021-04-10 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_intern',
            field=models.BooleanField(default=False),
        ),
    ]
