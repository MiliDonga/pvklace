# Generated by Django 3.0.8 on 2020-09-12 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvkadmin', '0003_auto_20200912_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='category',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 19, 29, 11, 360542)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 19, 29, 11, 360542)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 19, 29, 11, 361539)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 19, 29, 11, 361539)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 9, 12, 19, 29, 11, 361539)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='item_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 19, 29, 11, 359599)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 19, 29, 11, 359599)),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 19, 29, 11, 360542)),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 19, 29, 11, 360542)),
        ),
    ]
