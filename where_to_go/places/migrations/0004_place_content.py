# Generated by Django 4.2.3 on 2023-07-12 01:57

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_options_alter_image_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='content',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
    ]