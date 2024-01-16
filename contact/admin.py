from django.contrib import admin
from contact.models import Contact
from contact.models import Category

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show'
    ordering = '-id',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    # list_per_page = 1
    list_max_show_all = 100
    # list_editable = 'show',
    list_display_links = 'id',        #não pode por o mesmo campo em editable e display_links

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
    