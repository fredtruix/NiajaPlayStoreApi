# Generated by Django 4.0.4 on 2022-08-31 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nftapi', '0002_favorite_user_followers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='favorite',
        ),
        migrations.AlterField(
            model_name='user_details',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='username',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='website_link',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='User_followers',
        ),
    ]
