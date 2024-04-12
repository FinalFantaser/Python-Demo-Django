from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'date')
    list_display_links = ('id', 'name', 'phone')
    readonly_fields = ('id', 'name', 'phone', 'date')
    ordering = ('id', 'date')
    search_fields = ('phone', 'name')
    search_help_text = 'Имя или телефон'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_model_perms(self, request):
        return {'view': True, 'delete': True}

# Register your models here.
admin.site.register(Customer, CustomerAdmin)