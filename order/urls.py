from django.urls import path
from . import views


urlpatterns = [
    path('start-order/', views.start_order, name='start_order'),
]
