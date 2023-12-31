# Generated by Django 4.2.5 on 2023-09-14 11:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_lesson_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecertificate',
            name='certificate',
            field=models.FileField(upload_to='certificate/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt', 'csv', 'html', 'jpg', 'jpeg', 'png'])], verbose_name='Certificate'),
        ),
        migrations.AlterField(
            model_name='lessoncontent',
            name='file',
            field=models.FileField(upload_to='certificate/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg', 'mp4', 'avi', 'mov'])], verbose_name='Certificate'),
        ),
    ]
