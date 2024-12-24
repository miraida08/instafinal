# Generated by Django 5.1.4 on 2024-12-21 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_alter_userprofile_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='hashtag',
            new_name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description_ru',
            field=models.TextField(null=True),
        ),
    ]
