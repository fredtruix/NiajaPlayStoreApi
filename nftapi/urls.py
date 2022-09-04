from django.urls import path
from .apis import (Routes, get_User_NFT_favorite, get_or_create_account,
                   get_or_delete_favorite, get_or_update, get_or_create, _create_fovorites)

urlpatterns = [
    path('', Routes),
    path('create-account/<str:address>/', get_or_create_account),
    path('update/<str:address>/', get_or_update),
    path('create-followers/<str:user_id>/', get_or_create),
    path('create-favorite', _create_fovorites),
    path('get-user-favorite/<str:user_id>/', get_User_NFT_favorite),
    path('get-or-delete-favorite/<str:User_id>/<str:NFT_id>/', get_or_delete_favorite)
]
