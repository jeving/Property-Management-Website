from django.contrib import admin

from .models import Contact1

class Contact1Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'email', 'contact_date',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'message', 'phone', 'email', 'subject')
    list_per_page = 10

admin.site.register(Contact1, Contact1Admin)
