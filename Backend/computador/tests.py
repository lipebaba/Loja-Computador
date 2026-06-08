from django.test import TestCase

from .models import Computador
from .serializers import ComputadorSerializer


class ComputadorSerializerTests(TestCase):
    def test_serializer_accepts_valid_data(self):
        data = {
            'nome': 'Notebook Gamer',
            'descricao': 'Notebook com placa dedicada',
            'categoria': 'NOTEBOOK',
            'preco': '4999.90',
            'estoque': 5,
        }

        serializer = ComputadorSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        instance = serializer.save()
        self.assertEqual(instance.nome, data['nome'])
        self.assertEqual(instance.categoria, data['categoria'])
