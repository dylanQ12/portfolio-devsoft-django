# Generated by Django 5.1.1 on 2024-09-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_url_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_github',
            field=models.URLField(blank=True, null=True),
        ),
    ]