# Generated by Django 4.0.4 on 2022-08-31 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nftapi', '0005_alter_user_details_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='verifield',
            field=models.BooleanField(default=False),
        ),
    ]
