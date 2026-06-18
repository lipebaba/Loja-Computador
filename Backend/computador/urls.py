from django.urls import path
from .views import listar_produtos, obter_produto

urlpatterns = [
    path('produtos/', listar_produtos),
    path('produtos/<int:pk>/', obter_produto),
]