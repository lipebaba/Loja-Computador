from django.urls import path
from .views import ProdutoListCreateView, ProdutoDetailView

urlpatterns = [
    path('produtos/', ProdutoListCreateView.as_view(), name='produto-list'),
    path('produtos/<int:pk>/', ProdutoDetailView.as_view(), name='produto-detail'),
]