# Generated by Django 2.2.5 on 2020-03-11 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0013_auto_20200311_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='category',
            field=models.CharField(choices=[('category_web', 'category_web'), ('category_reversing', 'category_reversing'), ('category_steg', 'category_steg'), ('category_pwning', 'category_pwning'), ('category_misc', 'category_misc'), ('category_crypt', 'category_crypt')], default='category_steg', max_length=50),
        ),
    ]
