# Generated by Django 4.2.4 on 2023-08-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]