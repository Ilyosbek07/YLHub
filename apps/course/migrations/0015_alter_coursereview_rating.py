# Generated by Django 4.2.5 on 2023-09-18 08:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_remove_coursereview_user_course_coursereview_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursereview',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Rating'),
        ),
    ]
