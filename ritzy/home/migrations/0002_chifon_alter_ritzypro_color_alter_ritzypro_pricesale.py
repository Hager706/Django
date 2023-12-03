# Generated by Django 4.2.5 on 2023-09-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chifon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('namescarf', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('pricesale', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('ProductDescription', models.TextField()),
                ('Dimensions', models.TextField()),
                ('GarmentCare', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='ritzypro',
            name='color',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ritzypro',
            name='pricesale',
            field=models.CharField(max_length=255, null=True),
        ),
    ]