# Generated by Django 5.0.2 on 2024-02-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_university_application_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='letter',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
