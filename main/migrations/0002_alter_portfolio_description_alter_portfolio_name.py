# Generated by Django 4.2.7 on 2023-11-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]