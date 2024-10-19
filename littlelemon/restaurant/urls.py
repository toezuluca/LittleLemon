#define URL route for index() view
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index')
]
