# Generated by Django 3.2.12 on 2022-02-19 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='city',
            field=models.TextField(max_length=60),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='name',
            field=models.TextField(max_length=60),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.TextField(max_length=60),
        ),
        migrations.AlterField(
            model_name='screens',
            name='name',
            field=models.TextField(max_length=60),
        ),
    ]
