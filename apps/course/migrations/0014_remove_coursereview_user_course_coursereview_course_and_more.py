# Generated by Django 4.2.5 on 2023-09-18 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0013_alter_coursereview_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursereview',
            name='user_course',
        ),
        migrations.AddField(
            model_name='coursereview',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='course_review', to='course.usercourse', verbose_name='Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursereview',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
    ]
