# Generated by Django 5.0.2 on 2024-04-16 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_delete_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=datetime.datetime(2024, 4, 16, 16, 14, 6, 311441, tzinfo=datetime.timezone.utc), upload_to='books/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]