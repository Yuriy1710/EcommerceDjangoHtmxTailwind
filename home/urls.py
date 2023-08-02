from django.urls import path
from django.contrib.auth import views
from .views import *


urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('shop/', shop, name="shop"),
    path('signup/', signup, name="signup"),
    path('login/', views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('my-account/', my_account, name='my_account'),
    path('my-account/edit/', edit_my_account, name='edit_my_account'),
]

