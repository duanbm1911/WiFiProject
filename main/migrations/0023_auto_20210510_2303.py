# Generated by Django 3.2.1 on 2021-05-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20210506_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('student_code', models.IntegerField()),
                ('student_first_name', models.CharField(max_length=100)),
                ('student_last_name', models.CharField(max_length=100)),
                ('student_classmate', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='bw_download',
            field=models.IntegerField(default=10000, verbose_name='Băng thông download (Kbps)'),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='bw_upload',
            field=models.IntegerField(default=10000, verbose_name='Băng thông upload (Kbps)'),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='time_used',
            field=models.IntegerField(default=60, verbose_name='Thời gian sử dụng (Phút)'),
        ),
    ]
