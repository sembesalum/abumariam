# Generated by Django 3.2.7 on 2023-07-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20230722_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='half_day_booking',
            name='sex',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10),
        ),
    ]