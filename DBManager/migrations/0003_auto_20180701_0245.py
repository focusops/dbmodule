# Generated by Django 2.0.5 on 2018-06-30 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBManager', '0002_delete_basemodals'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='host',
            table='dbmanager_host',
        ),
    ]