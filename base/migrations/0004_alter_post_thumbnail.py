# Generated by Django 3.2 on 2023-06-09 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='placeholder1.jpeg', null=True, upload_to='images'),
        ),
    ]
