# Generated by Django 3.0.8 on 2020-07-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.AddField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]