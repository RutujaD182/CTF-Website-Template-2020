# Generated by Django 2.2.5 on 2020-03-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0019_auto_20200320_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='Hard',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='questions',
            name='Med',
            field=models.IntegerField(default=1),
        ),
    ]
