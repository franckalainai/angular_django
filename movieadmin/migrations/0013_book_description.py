# Generated by Django 3.2.6 on 2021-08-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieadmin', '0012_remove_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
