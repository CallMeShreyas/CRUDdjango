# from django.contrib import admin
from django.urls import path, include
from myapp import views
# from .models import Employee

urlpatterns = [
    path('', views.first),
    path('add', views.add),
    path('success', views.success),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete)
]
