# Generated by Django 4.0.4 on 2022-09-01 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nftapi', '0011_remove_user_followers_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nft_address', to='nftapi.user_details')),
                ('followers', models.ManyToManyField(to='nftapi.user_details')),
            ],
        ),
    ]
