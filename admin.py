from django.contrib import admin
from . models import product

class productadmin(admin.ModelAdmin):
    list_display=('name','price','stock','image')

# Register your models here.
admin.site.register(product,productadmin)