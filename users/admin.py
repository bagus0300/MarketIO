from django.contrib import admin
from .models import User, UserFavourite

admin.site.register(User)
admin.site.register(UserFavourite)
