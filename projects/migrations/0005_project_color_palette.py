# Generated by Django 3.2.4 on 2021-06-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='color_palette',
            field=models.BooleanField(default=False),
        ),
    ]