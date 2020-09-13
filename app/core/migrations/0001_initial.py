# Generated by Django 3.1 on 2020-09-13 04:45

import core.models.upload
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=16)),
                ('call_time', models.CharField(blank=True, choices=[('WEEK_DAY', 'WEEK_DAY'), ('WEEK_EVENING', 'WEEK_EVENING'), ('SATURDAY', 'SATURDAY'), ('SUNDAY', 'SUNDAY')], max_length=32, null=True)),
                ('is_eligible', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('full_name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=150)),
                ('phone_number', models.CharField(blank=True, default='', max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('topic', models.CharField(choices=[('REPAIRS', 'REPAIRS'), ('RENT_REDUCTION', 'RENT_REDUCTION'), ('OTHER', 'OTHER')], max_length=32)),
                ('answers', models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('complete', models.BooleanField(default=False)),
                ('is_alert_sent', models.BooleanField(default=False)),
                ('is_data_sent', models.BooleanField(default=False)),
                ('is_case_sent', models.BooleanField(default=False)),
                ('is_reminder_sent', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=core.models.upload.get_s3_key)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.submission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]