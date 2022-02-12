from django.urls import path
from .views import create_view, index

urlpatterns = [
    path('new', create_view, name='oportunidades_new'),
    path('test', index)
]