# Generated by Django 5.1.3 on 2024-11-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0002_user_otp_created_at_user_otp_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
