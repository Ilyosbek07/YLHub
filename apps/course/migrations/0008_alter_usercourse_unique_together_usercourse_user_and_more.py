# Generated by Django 4.2.5 on 2023-09-14 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0007_alter_coursecertificate_certificate_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usercourse',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile_user_course', to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='usercourse',
            unique_together={('user', 'course')},
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='profile',
        ),
    ]