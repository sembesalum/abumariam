# Generated by Django 3.2.7 on 2023-07-09 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_booking_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='fullname',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]