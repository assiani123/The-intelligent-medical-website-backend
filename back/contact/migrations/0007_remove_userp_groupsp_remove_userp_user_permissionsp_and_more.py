# Generated by Django 4.2.1 on 2023-05-18 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contact', '0006_userp_groupsp_userp_user_permissionsp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userp',
            name='groupsp',
        ),
        migrations.RemoveField(
            model_name='userp',
            name='user_permissionsp',
        ),
        migrations.AlterField(
            model_name='userp',
            name='groups',
            field=models.ManyToManyField(related_name='userps', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='userp',
            name='user_permissions',
            field=models.ManyToManyField(related_name='userps', to='auth.permission'),
        ),
    ]
