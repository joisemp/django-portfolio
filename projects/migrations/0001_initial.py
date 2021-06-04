# Generated by Django 3.2.4 on 2021-06-04 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('post_date', models.DateField(auto_now_add=True)),
                ('post_time', models.TimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/projects')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/projects')),
                ('case_study_file', models.FileField(blank=True, null=True, upload_to='files/projects/case_studies')),
            ],
        ),
    ]
