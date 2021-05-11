# Generated by Django 3.1.3 on 2021-04-17 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210416_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_mac', models.CharField(max_length=100)),
                ('client_ip', models.CharField(max_length=100)),
                ('ap_mac', models.CharField(max_length=100)),
                ('wifi_name', models.CharField(max_length=100)),
                ('wifi_channel', models.CharField(max_length=100)),
                ('wifi_rssi', models.CharField(max_length=100)),
                ('wifi_signal', models.CharField(max_length=100)),
                ('wifi_tx_bytes', models.CharField(max_length=100)),
                ('wifi_rx_bytes', models.CharField(max_length=100)),
            ],
        ),
    ]