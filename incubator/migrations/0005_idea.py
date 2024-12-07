# Generated by Django 5.1.3 on 2024-12-06 10:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0004_skill_profile_created_at_profile_github_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Tech', 'Tech'), ('Finance', 'Finance'), ('Health', 'Health'), ('Entertainment', 'Entertainment'), ('Food', 'Food')], max_length=100)),
                ('visibility', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ideas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
