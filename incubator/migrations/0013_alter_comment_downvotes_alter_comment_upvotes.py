# Generated by Django 5.1.3 on 2024-12-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0012_remove_comment_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='downvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
