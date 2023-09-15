# Generated by Django 4.2.5 on 2023-09-14 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tests', '0003_remove_variant_test_variant_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variant',
            options={'verbose_name': 'Variant', 'verbose_name_plural': 'Variants'},
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_true', models.BooleanField(default=False, verbose_name='Is True')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_question_answer', to='tests.question', verbose_name='Question')),
                ('selected_variant', models.ManyToManyField(related_name='user_variant', to='tests.variant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Answer',
                'verbose_name_plural': 'User Answers',
            },
        ),
    ]
