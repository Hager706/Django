# Generated by Django 4.2.5 on 2023-09-30 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_chifon_sold_alter_chifon_pricesale'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='image2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='pricesale',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='soldout',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]