# Generated by Django 2.2.1 on 2021-04-15 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210415_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='status',
            field=models.CharField(default='DEACTIVE', max_length=200),
        ),
    ]
