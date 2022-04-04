from django.urls import path
from .views import create_view, detail_view, edit_view, delete_view

urlpatterns = [
    path('new', create_view, name='oportunidades_new'),
    path('<int:pk>', detail_view, name='oportunidades_detail'),
    path('<int:pk>/edit', edit_view, name='oportunidades_edit'),
    path('<int:pk>/delete', delete_view, name='oportunidades_delete'),
]