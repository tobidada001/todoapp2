
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('somedata', views.somedata, name = 'somedata'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('confirm/<int:id>', views.confirm, name = 'confirm')
]
