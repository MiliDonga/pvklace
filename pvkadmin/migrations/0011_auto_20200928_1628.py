# Generated by Django 3.0.8 on 2020-09-28 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvkadmin', '0010_auto_20200928_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='about_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 204830)),
        ),
        migrations.AlterField(
            model_name='about_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 204830)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 201872)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 201872)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 204830)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 204830)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 203832)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 203832)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 202871)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 203832)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 201872)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 201872)),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 202871)),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 28, 59, 202871)),
        ),
    ]