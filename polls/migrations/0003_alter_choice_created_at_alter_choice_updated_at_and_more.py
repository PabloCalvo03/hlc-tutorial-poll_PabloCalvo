# Generated by Django 5.0 on 2024-01-10 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_created_at_choice_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 10, 8, 36, 1, 272043, tzinfo=datetime.timezone.utc), verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 10, 8, 36, 1, 272060, tzinfo=datetime.timezone.utc), verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 10, 8, 36, 1, 263813, tzinfo=datetime.timezone.utc), verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 10, 8, 36, 1, 263832, tzinfo=datetime.timezone.utc), verbose_name='updated at'),
        ),
    ]
