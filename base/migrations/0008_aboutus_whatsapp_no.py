# Generated by Django 3.2.7 on 2023-07-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20230720_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='whatsapp_no',
            field=models.CharField(default=11, max_length=200),
            preserve_default=False,
        ),
    ]
