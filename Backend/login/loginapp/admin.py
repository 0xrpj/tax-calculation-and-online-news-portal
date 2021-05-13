from django.contrib import admin

from .models import Post, Category, Tax, History

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tax)
admin.site.register(History)
