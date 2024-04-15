# Generated by Django 4.2.11 on 2024-04-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('image_description', models.TextField(blank=True)),
                ('content', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField()),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
    ]