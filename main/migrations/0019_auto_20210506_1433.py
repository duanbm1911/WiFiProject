# Generated by Django 3.1.3 on 2021-05-06 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210505_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='bw_download',
            field=models.IntegerField(default=1000000),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='bw_upload',
            field=models.IntegerField(default=1000000),
        ),
    ]
