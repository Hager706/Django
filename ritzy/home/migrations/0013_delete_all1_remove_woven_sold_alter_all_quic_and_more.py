# Generated by Django 4.2.5 on 2023-09-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_woven_image2_woven_sold_alter_all_quic_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='All1',
        ),
        migrations.RemoveField(
            model_name='woven',
            name='sold',
        ),
        migrations.AlterField(
            model_name='all',
            name='quic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chifon',
            name='status',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lycra',
            name='status',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='woven',
            name='material',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
