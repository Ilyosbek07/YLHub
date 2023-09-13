# Generated by Django 4.2.5 on 2023-09-13 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_remove_user_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=125, verbose_name='Name')),
                ('is_optional', models.BooleanField(default=False, verbose_name='Is Optional')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=125, verbose_name='Title')),
                ('desc', models.TextField(verbose_name='Description')),
                ('duration_time', models.IntegerField(verbose_name='Duration Time')),
                ('score', models.IntegerField(verbose_name='Score')),
                ('main_image', models.ImageField(upload_to='', verbose_name='Image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_category', to='course.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=125, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('type', models.CharField(choices=[('video', 'Video'), ('task', 'Task'), ('exam', 'Exam'), ('book', 'Book'), ('audiobook', 'Audio book')], max_length=55, verbose_name='Type')),
                ('order', models.IntegerField(verbose_name='Order')),
                ('points', models.IntegerField(verbose_name='Points')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_time', models.DateField(auto_now_add=True)),
                ('end_time', models.DateField(auto_now_add=True)),
                ('is_finish', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_course', to='course.course', verbose_name='Course')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user_course', to='users.profile', verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'User Course',
                'verbose_name_plural': 'User Courses',
                'unique_together': {('profile', 'course')},
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=125, verbose_name='Title')),
                ('file', models.FileField(upload_to='media/', verbose_name='File')),
                ('order', models.IntegerField(verbose_name='Order')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.lesson', verbose_name='Lesson')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='LessonProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_finish', models.BooleanField(default=False, verbose_name='Is Finish')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.lesson', verbose_name='Lesson')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Lesson Progress',
                'verbose_name_plural': 'Lesson Progress',
            },
        ),
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(verbose_name='Comment')),
                ('rating', models.PositiveIntegerField(verbose_name='Rating')),
                ('user_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='course.usercourse', verbose_name='User Course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('certificate', models.FileField(upload_to='', verbose_name='Certificate')),
                ('user_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_certificate', to='course.usercourse', verbose_name='User Course')),
            ],
            options={
                'verbose_name': 'Course Certificate',
                'verbose_name_plural': 'Course Certificates',
            },
        ),
    ]