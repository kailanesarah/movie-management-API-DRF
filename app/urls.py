from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do Swagger com suporte a Token Authentication
schema_view = get_schema_view(
    openapi.Info(
        title="API Movies",
        default_version='v1',
        description="Documentação da API com Swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kailanesarahpro@gmail.com"),
        license=openapi.License(name="Licença BSD"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],  # Evita erro de permissão global
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.url')),
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('review.urls')),

    # URLs do Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
