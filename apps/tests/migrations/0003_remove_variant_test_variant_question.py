# Generated by Django 4.2.5 on 2023-09-14 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_questioncontent_usertest_variant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='test',
        ),
        migrations.AddField(
            model_name='variant',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question_variant', to='tests.question', verbose_name='Question'),
            preserve_default=False,
        ),
    ]