# Generated by Django 2.2.2 on 2019-06-15 02:50

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_submission_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='data',
        ),
        migrations.AddField(
            model_name='submission',
            name='answers',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, encoder=django.core.serializers.json.DjangoJSONEncoder),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='questions',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, encoder=django.core.serializers.json.DjangoJSONEncoder),
            preserve_default=False,
        ),
    ]
