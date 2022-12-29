# Generated by Django 3.0.8 on 2020-10-02 07:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pvkadmin', '0016_auto_20201002_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 870153)),
        ),
        migrations.AlterField(
            model_name='about_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 870153)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 868153)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 868153)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 870153)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 870153)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 869160)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 869160)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 869160)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 869160)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 867156)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 867156)),
        ),
        migrations.AlterField(
            model_name='product_photo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 867156)),
        ),
        migrations.AlterField(
            model_name='product_photo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pvkadmin.product'),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 868153)),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 12, 48, 27, 868153)),
        ),
    ]
