from django.contrib import admin

from .models import Post, Category, Tax, History, TaxOne

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tax)
admin.site.register(TaxOne)
admin.site.register(History)
