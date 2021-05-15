
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
urlpatterns = [
    # url for admin page
    path('admin/', admin.site.urls),
    # path for custom urls
    path('', include('loginapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'loginapp.views.error_404'
