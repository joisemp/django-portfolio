# Generated by Django 3.2.4 on 2021-06-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_remove_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[], default='Figma', max_length=255),
        ),
    ]
