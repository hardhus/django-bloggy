# Generated by Django 4.2.4 on 2023-08-11 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_image_post_tag_post_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.CharField(default="test", max_length=100),
            preserve_default=False,
        ),
    ]
