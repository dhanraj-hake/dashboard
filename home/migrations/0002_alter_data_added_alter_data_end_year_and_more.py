# Generated by Django 4.0.2 on 2022-10-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='added',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='data',
            name='end_year',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='data',
            name='published',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='data',
            name='start_year',
            field=models.CharField(max_length=50),
        ),
    ]