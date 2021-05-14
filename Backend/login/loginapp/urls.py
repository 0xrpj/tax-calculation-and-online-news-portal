from django.urls import path
from . import views
# importimg created views
from .views import HomeView, PoliticsView, EntertainmentView, SportsView, BusinessView, AboutView, Detail_Article_View, AddPostView, UpdatePostView, DeletePostView

# url for browser to shows views with its access name for views
urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('', views.loginPage, name="login"),
    path('accounts/login/', views.loginPageRedirect, name="loginRedirect"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', HomeView.as_view(), name="home"),
    path('politics/', PoliticsView.as_view(), name="politics"),
    path('entertainment/', EntertainmentView.as_view(), name="entertainment"),
    path('sports/', SportsView.as_view(), name="sports"),
    path('business/', BusinessView.as_view(), name="business"),
    path('about/', views.AboutView, name="about"),
    path('search/', views.search, name="search"),

    # path('blog/', Blog.as_view(), name="Blog"),
    path('article/<int:pk>', Detail_Article_View.as_view(), name="article-detail"),
    path('article/<int:pk>/update/', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name="delete_post"),
    path('dashboard/', AddPostView.as_view(), name='dashboard'),

    # tax calculation
    path('tax/', views.Tax_calculator, name="Tax_calculator"),
    path('history/', views.Tax_History, name="Tax_History")

]
