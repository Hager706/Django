# Generated by Django 4.2.5 on 2023-09-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_woven_quic_woven_sold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ctag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('link', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='woven',
            name='pricesale',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]