# Generated by Django 3.1.3 on 2021-05-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_userinformation_time_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='bw_download',
            field=models.IntegerField(default=10000),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='bw_upload',
            field=models.IntegerField(default=10000),
        ),
    ]
