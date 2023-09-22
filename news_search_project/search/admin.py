from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser, SearchResult

# Register your models here.
class CustomUserAdmin(UserAdmin):
    """
    Admin interface for custom user management.

    This admin class extends Django's UserAdmin,
    to provide custom user management functionality.
    It allows administrators to toggle the blocking status of users.

    Attributes:
        add_form (type): The form class for adding a new custom user.
        model (type): The custom user model associated with this admin.
        list_display (list): The list of fields to display in the admin list view.

    Methods:
        toggle_block(self, request, queryset): Toggles the blocking status of selected users.
    """
    
    
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ["username", "is_blocked"]

    def toggle_block(self, request, queryset):
        for user in queryset:
            user.is_blocked = not user.is_blocked
            user.save()

    toggle_block.short_description = 'Toggle user block/unblock'

    actions = [toggle_block]

# Registered models with Admin Site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SearchResult)
