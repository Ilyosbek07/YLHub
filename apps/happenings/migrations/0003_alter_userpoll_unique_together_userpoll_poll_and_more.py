# Generated by Django 4.2.5 on 2023-09-16 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_document_file_document_certificate'),
        ('happenings', '0002_alter_pollchoice_options_pollchoice_order'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userpoll',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='userpoll',
            name='poll',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_choices', to='happenings.poll', verbose_name='Poll'),
        ),
        migrations.AlterUniqueTogether(
            name='userpoll',
            unique_together={('profile', 'poll')},
        ),
    ]
