# Generated by Django 2.2 on 2019-04-09 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='course',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
