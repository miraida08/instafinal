# Generated by Django 5.1.4 on 2024-12-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_rename_hashtag_post_description_post_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hashtag',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
