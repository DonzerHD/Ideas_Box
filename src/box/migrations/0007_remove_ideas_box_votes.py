# Generated by Django 4.1 on 2023-03-23 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("box", "0006_ideas_box_votes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ideas_box",
            name="votes",
        ),
    ]