from django.urls import path
from . import views


urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('shop/', views.shop, name="shop"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
]

