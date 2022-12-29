# Generated by Django 3.0.8 on 2020-10-02 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvkadmin', '0014_auto_20201002_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 977968)),
        ),
        migrations.AlterField(
            model_name='about_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 977968)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 968593)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 968593)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 977968)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 977968)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 972672)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 972672)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 972672)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 977968)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 968593)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 968593)),
        ),
        migrations.AlterField(
            model_name='product_photo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 968593)),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 972672)),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 34, 16, 972672)),
        ),
    ]
