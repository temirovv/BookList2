from django.urls import path
from .views import index, delete, update, create


urlpatterns = [
    path('', index, name='books.home'),
    path('add/', create, name='books.create'),
    path('delete/<int:pk>', delete, name='books.delete'),
    path('update/<int:pk>', update, name='books.update')
]
