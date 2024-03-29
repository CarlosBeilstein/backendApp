# Generated by Django 5.0.1 on 2024-01-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backendApp', '0005_delete_favstocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavStocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('companyName', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('added', models.BooleanField(verbose_name=False)),
                ('change', models.FloatField()),
                ('changePer', models.FloatField()),
                ('movement', models.CharField(max_length=255)),
            ],
        ),
    ]
