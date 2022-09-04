from django.contrib import admin
from .models import User_details, User_followers, User_favorite

# Register your models here.
admin.site.register(User_details)
admin.site.register(User_followers)
admin.site.register(User_favorite)
