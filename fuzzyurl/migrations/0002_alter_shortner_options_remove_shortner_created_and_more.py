# Generated by Django 4.0 on 2021-12-20 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuzzyurl', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortner',
            options={},
        ),
        migrations.RemoveField(
            model_name='shortner',
            name='created',
        ),
        migrations.RemoveField(
            model_name='shortner',
            name='times_follow',
        ),
    ]
