# Generated by Django 4.2 on 2023-04-25 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reduce', '0002_logurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlredirect',
            name='slug',
        ),
    ]