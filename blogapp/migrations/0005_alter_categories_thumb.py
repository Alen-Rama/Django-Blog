# Generated by Django 4.0.1 on 2022-02-12 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_categories_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='thumb',
            field=models.ImageField(default=None, upload_to='categories'),
        ),
    ]