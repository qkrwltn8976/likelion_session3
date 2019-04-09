from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name="add"),
    path('list/', views.list, name="list"),
    path('edit/', views.edit, name="edit"),
    path('list/detail/', views.detail, name="detail"),
]