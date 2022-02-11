from django.urls import path
from .views import create_view

urlpatterns = [
    path('new', create_view, name='oportunidades_new'),
]