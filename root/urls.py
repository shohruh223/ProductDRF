from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="drf_begin",
      default_version='v1',
      description="drf dan start boshladim",
      terms_of_service="https://github.com/shohruh223",
      contact=openapi.Contact(email="shohruh.abd2223@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swag'
                                                                  'ger-ui'),
   path('api-auth/', include('rest_framework.urls')),
   path('', include('app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


