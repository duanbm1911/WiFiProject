# Generated by Django 2.2.1 on 2021-04-15 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210415_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='email',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]