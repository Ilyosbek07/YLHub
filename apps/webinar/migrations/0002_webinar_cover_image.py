# Generated by Django 4.2.5 on 2023-09-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinar',
            name='cover_image',
            field=models.ImageField(default='webinar_default.png', upload_to='webinar/covers/', verbose_name='Cover image'),
        ),
    ]
