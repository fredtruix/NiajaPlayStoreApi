from django.urls import path
from .apis import (Routes, get_User_NFT_favorite, get_env_strings, get_or_create_account,
                   get_or_delete_favorite, get_or_update, get_or_create, _create_fovorites)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="NFT API",
        default_version='v1',
        description="Get all data on  NFT",
        terms_of_service="https://link.medium.com/sQFZhouMgmb",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="NFT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('create-account/<str:address>/', get_or_create_account),
    path('update/<str:address>/', get_or_update),
    path('create-followers/<str:user_id>/', get_or_create),
    path('create-favorite', _create_fovorites),
    path('get-user-favorite/<str:user_id>/', get_User_NFT_favorite),
    path('get-or-delete-favorite/<str:User_id>/<str:NFT_id>/', get_or_delete_favorite),
    path('key/', get_env_strings)
]
