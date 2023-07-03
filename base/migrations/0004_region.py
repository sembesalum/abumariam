# Generated by Django 3.2.7 on 2023-07-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_bluesafari_tour_company_contact_halfday_tour_island_tour_testimonial_tour_guides_zanzibar_shallow_za'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('discription', models.TextField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
    ]
