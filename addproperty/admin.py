from django.contrib import admin

from .models import AddProperty

class AddPropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'property_owner')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price', 'address', 'city', 'state')
    list_per_page = 10

admin.site.register(AddProperty, AddPropertyAdmin)
