# Generated by Django 5.0.1 on 2024-01-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]