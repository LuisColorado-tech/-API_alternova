from django.conf import settings
from drf_yasg import openapi

info = openapi.Info(
    title="API de Streaming",
    default_version='v1',
    description="API para el acceso a películas y series de una plataforma de streaming",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="contact@streamingapi.local"),
    license=openapi.License(name="MIT License"),
)

SWAGGER_INFO = info
