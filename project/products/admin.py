from django.contrib import admin
from .models import Product, Test

# Register your models here.
admin.site.register(Test)
admin.site.site_header = 'Header'
admin.site.site_title = 'Header'
# admin.site.site_header = 'Header'

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_display_links = ['name']
    list_editable = ['price']
    search_fields = ['name']
    list_filter = ['category']
    fields = ['name', 'price'] # appear in each obj
    #ال يتكتب فى لينك مايتكتبش فى ايدت

admin.site.register(Product, ProductAdmin)
# admin.site.register()


