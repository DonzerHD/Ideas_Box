# Generated by Django 4.1 on 2023-03-23 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("box", "0004_vote"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Vote",
        ),
    ]
