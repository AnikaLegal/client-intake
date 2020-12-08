# Generated by Django 3.1.4 on 2020-12-08 06:20

from django.db import migrations


def migrate_client_data(apps, schema_editor):
    """
    We can't import the Post model directly as it may be a newer
    version than this migration expects. We use the historical version.
    """
    Client = apps.get_model("core", "Client")
    for client in Client.objects.all():
        # Migrate call times.
        if client.call_time:
            client.call_times = [client.call_time]

        weekly_income = None
        for issue in client.issue_set.all():
            if "CLIENT_WEEKLY_EARNINGS" in issue.answers:
                weekly_income = issue.answers["CLIENT_WEEKLY_EARNINGS"]

            if "CLIENT_SPECIAL_CIRCUMSTANCES" in issue.answers:
                pass
                # CLIENT_SPECIAL_CIRCUMSTANCES

        if weekly_income is not None:
            client.weekly_income = weekly_income

        client.save()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_auto_20201208_1713"),
    ]

    operations = [
        migrations.RunPython(migrate_client_data),
    ]
