# Generated by Django 3.1.3 on 2020-11-27 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_issue_is_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.issue'),
        ),
    ]
