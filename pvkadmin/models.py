from django.db import models
import datetime
# Create your models here.

class product(models.Model):
    product_image = models.ImageField(upload_to='production/product')
    product_name = models.CharField(max_length=30)
    product_description = models.TextField()
    category = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())

class product_photo(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='production/product')
    created_at = models.DateTimeField(default=datetime.datetime.now())

class category(models.Model):
    category_image = models.ImageField(upload_to='production/category')
    category_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())

class team(models.Model):
    member_image = models.ImageField(upload_to='production/team')
    member_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())

class inquiry(models.Model):
    name = models.TextField()
    email = models.TextField()
    contact_no = models.BigIntegerField()
    item_name = models.CharField(max_length=30, blank=True)
    status = models.BooleanField(default=False)
    category = models.CharField(max_length=30, blank=True)
    created_at = models.DateField(default=datetime.datetime.now())

class home_banner(models.Model):
    banner_image = models.ImageField(upload_to='production/home_banner')
    link = models.TextField(default="")
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())

class order(models.Model):
    inquiry_id = models.IntegerField()
    item_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.datetime.now())

class about_banner(models.Model):
    banner_image = models.ImageField(upload_to='production/about_us')
    text = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())

class contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    contact_no = models.BigIntegerField()
    message = models.TextField(default="")
    subject = models.TextField(default="")
    status = models.BooleanField(default=False)
    created_at = models.DateField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())