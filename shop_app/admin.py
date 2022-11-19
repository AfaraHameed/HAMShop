from django.contrib import admin
from . models import *
# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name' , 'slug']
admin.site.register(categ,catadmin)

class productadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','image']
    list_editable = ['price' , 'stock' , 'image']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(products,productadmin)