# Generated by Django 4.0.4 on 2022-05-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='date_filmed',
            field=models.DateField(auto_now_add=True),
        ),
    ]
