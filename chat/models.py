from django.db import models

# Create your models here.
from django.db import models
from accounts.views import User
class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_messages')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_from_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.admin.username}: {self.message[:50]}'
