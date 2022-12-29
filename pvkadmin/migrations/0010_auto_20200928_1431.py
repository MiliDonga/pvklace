# Generated by Django 3.0.8 on 2020-09-28 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvkadmin', '0009_auto_20200928_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_banner',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
        migrations.AlterField(
            model_name='about_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 662145)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 662145)),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 14, 31, 59, 666111)),
        ),
    ]
