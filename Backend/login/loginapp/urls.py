from django.urls import path
from . import views
from .views import HomeView, Blog, Detail_Article_View, AddPostView , UpdatePostView ,DeletePostView


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', HomeView.as_view(), name="home"),
    path('blog/', Blog.as_view(), name="Blog"),
    path('article/<int:pk>', Detail_Article_View.as_view(), name="article-detail"),
    path('article/<int:pk>/update/',UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete/',DeletePostView.as_view(), name="delete_post"),
    path('dashboard/', AddPostView.as_view(), name='dashboard')
]
