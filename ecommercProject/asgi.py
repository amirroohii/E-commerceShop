"""
ASGI config for ecommercProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from chat import routing
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddleware, AuthMiddlewareStack
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommercProject.settings')

application = get_asgi_application()
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommercProject.settings')
# django_asgi_app = get_asgi_application()
#
# application = ProtocolTypeRouter(
#     {
#         'http': django_asgi_app,
#         'websocket': AuthMiddlewareStack(
#             URLRouter(
#                 routing.websocket_urlpatterns
#             )
#         )
#     }
# )