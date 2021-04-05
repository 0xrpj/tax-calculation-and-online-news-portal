from django.urls import path
from . import views
from .views import Blog, Detail_Article_View, AddPostView


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.homePage, name="home"),
    path('blog/', Blog.as_view(), name="Blog"),
    path('article/<int:pk>', Detail_Article_View.as_view(), name="article-detail"),
    path('dashboard/', AddPostView.as_view(), name='dashboard')
]
