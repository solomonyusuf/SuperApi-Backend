# Generated by Django 3.2.11 on 2022-05-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220427_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='sermon',
            name='artist',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='artist',
            field=models.CharField(max_length=225, null=True),
        ),
    ]