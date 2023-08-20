from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .forms import Login

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.SignupView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='SignupLogin.html', authentication_form=Login), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('shop/', views.ShopView.as_view(), name='shop'),
]
