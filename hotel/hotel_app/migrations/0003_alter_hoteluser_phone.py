# Generated by Django 4.0 on 2021-12-26 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0002_alter_host_options_alter_visitor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoteluser',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Phone'),
        ),
    ]
