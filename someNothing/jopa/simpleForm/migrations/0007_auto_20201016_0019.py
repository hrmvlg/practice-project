# Generated by Django 3.1.1 on 2020-10-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleForm', '0006_auto_20201015_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musictrack',
            name='track',
            field=models.FileField(blank=True, upload_to='tracks/'),
        ),
    ]
