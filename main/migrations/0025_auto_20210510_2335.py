# Generated by Django 3.2.1 on 2021-05-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20210510_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinformation',
            name='student_code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentinformation',
            name='student_id',
            field=models.CharField(max_length=100),
        ),
    ]
