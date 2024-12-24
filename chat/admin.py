from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'admin', 'message', 'timestamp', 'is_from_admin')
    list_filter = ('is_from_admin', 'timestamp')
    search_fields = ('user__username', 'admin__username', 'message')
    readonly_fields = ('timestamp',)

    def has_add_permission(self, request):
        return False  # جلوگیری از افزودن پیام از طریق پنل ادمین

    def has_change_permission(self, request, obj=None):
        return False  # جلوگیری از تغییر پیام‌های موجود
