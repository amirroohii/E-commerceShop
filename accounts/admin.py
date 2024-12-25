from django.contrib import admin
from .models import User
# Register your models here.
# admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'is_superuser')

admin.site.register(User, UserAdmin)