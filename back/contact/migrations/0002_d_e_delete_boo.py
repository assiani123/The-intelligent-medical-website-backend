# Generated by Django 4.2.1 on 2023-05-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='D',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='E',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dep', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Boo',
        ),
    ]
