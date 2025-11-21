"""
URL configuration for messaging_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# Import JWT views if available; avoid import-time failures when package isn't installed.
try:
    from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
    _JWT_AVAILABLE = True
except Exception:
    _JWT_AVAILABLE = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),  # include our app API
    # include DRF login/logout views for the browsable API
    path('api-auth/', include('rest_framework.urls')),
]

# Add JWT token endpoints only when simplejwt is installed.
if _JWT_AVAILABLE:
    urlpatterns += [
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]

