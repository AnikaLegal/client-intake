# Generated by Django 3.1 on 2020-09-13 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.client'),
            preserve_default=False,
        ),
    ]
