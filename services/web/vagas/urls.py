from django.urls import path
from .views import create_view, detail_view

urlpatterns = [
    path('new', create_view, name='oportunidades_new'),
    path('<int:pk>', detail_view, name='oportunidades_detail'),
]