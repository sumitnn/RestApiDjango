# Generated by Django 3.2.8 on 2021-10-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='sumit', max_length=30),
        ),
    ]
