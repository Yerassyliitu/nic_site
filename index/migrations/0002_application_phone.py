# Generated by Django 5.0.2 on 2024-02-16 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]