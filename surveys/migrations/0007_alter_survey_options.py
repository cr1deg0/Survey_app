# Generated by Django 4.2.7 on 2023-12-05 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0006_rename_creator_survey_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='survey',
            options={'ordering': ['-created'], 'permissions': (('view_own_survey', 'View own survey'),)},
        ),
    ]
