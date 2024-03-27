# Generated by Django 4.2.2 on 2024-03-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Isbn', models.IntegerField()),
                ('Author', models.TextField()),
                ('Title', models.TextField()),
                ('Category_name', models.CharField(max_length=50)),
                ('Category_id', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Fixed_Price', models.BooleanField()),
                ('Pub_date', models.DateField()),
            ],
        ),
    ]