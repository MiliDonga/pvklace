# Generated by Django 3.0.8 on 2020-10-02 06:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pvkadmin', '0012_auto_20201002_0912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image_1',
            new_name='product_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_image_2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_image_3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_image_4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_image_5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_image_6',
        ),
        migrations.AlterField(
            model_name='about_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 97865)),
        ),
        migrations.AlterField(
            model_name='about_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 97865)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 93912)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 93912)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 97865)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 97865)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 93912)),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 93912)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 93912)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 97865)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 93912)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 93912)),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 93912)),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 93912)),
        ),
        migrations.CreateModel(
            name='product_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 49, 30, 93912))),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pvkadmin.product')),
            ],
        ),
    ]
