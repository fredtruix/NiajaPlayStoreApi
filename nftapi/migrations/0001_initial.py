# Generated by Django 4.0.4 on 2022-08-30 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Untiled', max_length=300)),
                ('address', models.CharField(max_length=400, unique=True)),
                ('bio', models.TextField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('website_link', models.URLField(unique=True)),
                ('profile_image', models.ImageField(upload_to='')),
                ('profile_header_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
