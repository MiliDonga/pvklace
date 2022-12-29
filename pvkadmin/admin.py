from django.contrib import admin

# Register your models here.
from pvkadmin.models import home_banner, inquiry, about_banner

admin.site.register(home_banner)
admin.site.register(inquiry)
admin.site.register(about_banner)