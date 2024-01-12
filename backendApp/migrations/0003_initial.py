# Generated by Django 5.0.1 on 2024-01-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backendApp', '0002_delete_favstocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavStocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('change', models.FloatField()),
                ('changePer', models.FloatField()),
            ],
        ),
    ]
