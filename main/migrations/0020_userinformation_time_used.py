# Generated by Django 3.1.3 on 2021-05-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210506_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='time_used',
            field=models.IntegerField(default=60),
        ),
    ]