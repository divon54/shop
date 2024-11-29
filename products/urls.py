from django.urls import path
from.import views

urlpatterns = [
    path('', views.insert, name='insert'),  # Route for inserting a new product
]
