# Generated by Django 3.0.8 on 2020-09-28 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvkadmin', '0007_auto_20200928_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 501271)),
        ),
        migrations.AlterField(
            model_name='about_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 501271)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 499199)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 499199)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 500275)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 500275)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 501271)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 501271)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 500275)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 497734)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 497734)),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 499199)),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 11, 47, 11, 499199)),
        ),
    ]