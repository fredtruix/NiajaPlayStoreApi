# Generated by Django 4.0.4 on 2022-08-31 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nftapi', '0008_alter_user_favorite_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='profile_header_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
