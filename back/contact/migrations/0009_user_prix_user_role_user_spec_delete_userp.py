# Generated by Django 4.2.1 on 2023-05-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_alter_userp_options_alter_userp_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='prix',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='rr', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='spec',
            field=models.CharField(default='rrrrr', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Userp',
        ),
    ]