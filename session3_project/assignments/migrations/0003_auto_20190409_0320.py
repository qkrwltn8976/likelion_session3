# Generated by Django 2.2 on 2019-04-09 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_auto_20190409_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
