# Generated by Django 4.0.4 on 2022-08-30 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nftapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=400)),
                ('favorites', models.JSONField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=400)),
                ('followers', models.ManyToManyField(to='nftapi.user_details')),
            ],
        ),
    ]
