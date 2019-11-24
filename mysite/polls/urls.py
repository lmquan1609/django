from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('arb/', views.function1, name='fn')
]