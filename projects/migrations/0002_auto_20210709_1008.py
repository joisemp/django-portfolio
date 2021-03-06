# Generated by Django 3.2.4 on 2021-07-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='case_study_file',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(blank=True, default='Figma', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='file',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
