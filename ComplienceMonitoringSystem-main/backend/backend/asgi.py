import os
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from management.routing import websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
})