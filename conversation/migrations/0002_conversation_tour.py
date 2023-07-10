# Generated by Django 3.2.7 on 2023-07-10 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_booking_fullname'),
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='tour',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='base.toursite'),
            preserve_default=False,
        ),
    ]
