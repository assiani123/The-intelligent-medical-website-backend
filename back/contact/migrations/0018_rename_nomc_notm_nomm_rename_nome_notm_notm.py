# Generated by Django 4.2.1 on 2023-05-23 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0017_remove_notm_mesg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notm',
            old_name='nomc',
            new_name='nomm',
        ),
        migrations.RenameField(
            model_name='notm',
            old_name='nome',
            new_name='notm',
        ),
    ]
