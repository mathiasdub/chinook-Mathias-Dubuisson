# Generated by Django 4.2 on 2025-03-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='composer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
