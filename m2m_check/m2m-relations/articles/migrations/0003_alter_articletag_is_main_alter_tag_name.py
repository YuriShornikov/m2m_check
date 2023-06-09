# Generated by Django 4.1.7 on 2023-05-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_articletag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletag',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
