# Generated by Django 3.2.6 on 2021-08-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieadmin', '0006_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=36, unique=True),
        ),
    ]
