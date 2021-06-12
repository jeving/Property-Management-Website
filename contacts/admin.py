from django.contrib import admin

from .models import Contact,ContactAdd

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 10

admin.site.register(Contact, ContactAdmin)

class ContactAddAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'addproperty1', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'addproperty1')
    list_per_page = 10

admin.site.register(ContactAdd, ContactAddAdmin)
