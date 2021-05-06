from django.contrib import admin

from .models import Post, Category, Tax

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tax)
