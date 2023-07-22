# Generated by Django 3.2.7 on 2023-07-20 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20230710_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='client_image',
            field=models.ImageField(blank=True, null=True, upload_to='testmonial/'),
        ),
        migrations.AddField(
            model_name='tour_guides',
            name='guider_image',
            field=models.ImageField(blank=True, null=True, upload_to='guider/'),
        ),
    ]