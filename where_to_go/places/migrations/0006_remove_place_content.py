# Generated by Django 4.2.3 on 2023-07-12 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_description_long'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='content',
        ),
    ]
