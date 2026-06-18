from django.http import JsonResponse
from .models import Produto

def listar_produtos(request):
    produtos = list(Produto.objects.all().values())
    return JsonResponse(produtos, safe=False)

def obter_produto(request, pk):
    try:
        produto = Produto.objects.filter(id=pk).values().first()

        if produto:
            return JsonResponse(produto)

        return JsonResponse(
            {"erro": "Produto não encontrado"},
            status=404
        )

    except Exception as e:
        return JsonResponse(
            {"erro": str(e)},
            status=500
        )