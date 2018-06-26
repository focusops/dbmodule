# Generated by Django 2.0.5 on 2018-06-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ip', models.CharField(max_length=255)),
                ('cpu', models.CharField(max_length=255)),
                ('mem', models.CharField(max_length=255)),
                ('disk', models.CharField(max_length=255)),
                ('idc', models.CharField(max_length=255)),
                ('rootpwd', models.CharField(max_length=255)),
                ('readpwd', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=255)),
                ('createdTime', models.DateField(auto_now_add=True)),
                ('root', models.CharField(max_length=255)),
                ('read', models.CharField(max_length=255)),
                ('comment', models.TextField()),
            ],
        ),
    ]
