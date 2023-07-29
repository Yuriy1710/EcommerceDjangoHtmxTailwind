from django.urls import path
from . import views


urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('shop/', views.shop, name="shop"),
]

