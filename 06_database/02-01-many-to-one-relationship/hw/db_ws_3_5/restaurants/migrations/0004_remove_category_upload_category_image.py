# Generated by Django 4.2.11 on 2024-04-09 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_alter_category_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='upload',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
