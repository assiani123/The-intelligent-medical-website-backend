# Generated by Django 4.2.1 on 2023-05-23 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0016_notm_notp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notm',
            name='mesg',
        ),
    ]
