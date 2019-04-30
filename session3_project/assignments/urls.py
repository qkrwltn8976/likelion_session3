from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name="add"),
    path('list/', views.list, name="list"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('delete/<int:id>/', views.delete, name="delete"),
]