# Generated by Django 4.2.5 on 2023-09-16 07:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_remove_document_file_document_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modified time')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('cover_image', models.ImageField(upload_to='library/covers/', verbose_name='Cover image')),
                ('publication_year', models.PositiveSmallIntegerField(verbose_name='Publication year')),
                ('is_required', models.BooleanField(default=False, verbose_name='Is required')),
                ('is_recommended', models.BooleanField(default=False, verbose_name='Is recommended')),
                ('description', models.TextField(max_length=800, verbose_name='Description')),
                ('bonus_points', models.PositiveSmallIntegerField(default=0, verbose_name='Bonus points')),
                ('language', models.CharField(choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English')], max_length=2, verbose_name='Language')),
                ('duration', models.PositiveIntegerField(blank=True, verbose_name='Duration')),
            ],
            options={
                'verbose_name': 'Audiobook',
                'verbose_name_plural': 'Audiobooks',
            },
        ),
        migrations.CreateModel(
            name='AudioSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='Order')),
                ('duration', models.PositiveIntegerField(blank=True, verbose_name='Duration')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('audiobook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='library.audiobook', verbose_name='Audiobook')),
            ],
            options={
                'verbose_name': 'Audiobook section',
                'verbose_name_plural': 'Audiobook sections',
                'unique_together': {('order', 'audiobook')},
            },
        ),
        migrations.CreateModel(
            name='AudioUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='Order')),
                ('duration', models.PositiveSmallIntegerField(blank=True, verbose_name='Duration')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('audio_file', models.FileField(upload_to='library/files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])], verbose_name='File')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='library.audiosection', verbose_name='Section')),
            ],
            options={
                'verbose_name': 'Audiobook unit',
                'verbose_name_plural': 'Audiobook units',
                'unique_together': {('order', 'section')},
            },
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100, verbose_name='Full name')),
                ('birth_date', models.DateField(verbose_name='Birth date')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('about', models.TextField(max_length=1000, verbose_name='About')),
                ('avatar', models.ImageField(upload_to='library/authors/', verbose_name='Avatar')),
            ],
            options={
                'verbose_name': 'Book Author',
                'verbose_name_plural': 'Book Authors',
            },
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('is_popular', models.BooleanField(default=True, verbose_name='Is popular')),
                ('icon', models.FileField(upload_to='library/category/', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Book category',
                'verbose_name_plural': 'Book categories',
            },
        ),
        migrations.CreateModel(
            name='LibrarySearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('keyword', models.CharField(max_length=100, verbose_name='Search keyword')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='library_search_history', to='users.profile', verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Library Search History',
                'verbose_name_plural': 'Library Search Histories',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modified time')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('cover_image', models.ImageField(upload_to='library/covers/', verbose_name='Cover image')),
                ('publication_year', models.PositiveSmallIntegerField(verbose_name='Publication year')),
                ('is_required', models.BooleanField(default=False, verbose_name='Is required')),
                ('is_recommended', models.BooleanField(default=False, verbose_name='Is recommended')),
                ('description', models.TextField(max_length=800, verbose_name='Description')),
                ('bonus_points', models.PositiveSmallIntegerField(default=0, verbose_name='Bonus points')),
                ('language', models.CharField(choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English')], max_length=2, verbose_name='Language')),
                ('deadline', models.DateField(verbose_name='Deadline')),
                ('book_file', models.FileField(upload_to='library/files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='File')),
                ('pages', models.PositiveSmallIntegerField(blank=True, verbose_name='Pages')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='library.bookauthor', verbose_name='Author')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='library.bookcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.AddField(
            model_name='audiobook',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audiobooks', to='library.bookauthor', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='audiobook',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audiobooks', to='library.bookcategory', verbose_name='Category'),
        ),
        migrations.CreateModel(
            name='UserBookProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_page', models.PositiveSmallIntegerField(verbose_name='Last page')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_progresses', to='library.book', verbose_name='Book')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_progresses', to='users.profile', verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'User Book Progress',
                'verbose_name_plural': 'User Book Progresses',
                'unique_together': {('book', 'profile')},
            },
        ),
        migrations.CreateModel(
            name='UserAudiobookProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pause_time', models.PositiveSmallIntegerField(verbose_name='Pause time')),
                ('duration_so_far', models.PositiveIntegerField(blank=True, verbose_name='Total listened duration')),
                ('audio_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_progresses', to='library.audiounit', verbose_name='Audio unit')),
                ('audiobook', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_progresses', to='library.audiobook', verbose_name='Audio book')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audiobook_progresses', to='users.profile', verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'User audiobook progress',
                'verbose_name_plural': 'User audiobook progresses',
                'unique_together': {('profile', 'audiobook')},
            },
        ),
    ]
