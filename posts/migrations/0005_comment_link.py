# Generated by Django 3.1 on 2020-12-16 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]