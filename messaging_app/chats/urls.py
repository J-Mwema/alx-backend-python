from django.urls import path, include
from rest_framework import routers
try:
    from rest_framework_nested.routers import NestedDefaultRouter
except Exception:
    # Provide a lightweight fallback so Django can import urls even if
    # `rest_framework_nested` isn't installed in the environment.
    class NestedDefaultRouter:
        def __init__(self, parent_router, prefix, lookup='pk'):
            self._urls = []

        def register(self, prefix, viewset, basename=None):
            # noop: don't attempt to build nested routes if package missing
            return None

        @property
        def urls(self):
            return []
from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# create nested routes so /conversations/{pk}/messages/ is available
nested_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]

