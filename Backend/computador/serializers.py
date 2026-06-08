from rest_framework import serializers

from .models import Computador, Produto


class ComputadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computador
        fields = '__all__'


class ProdutoSerializer(ComputadorSerializer):
    class Meta(ComputadorSerializer.Meta):
        model = Produto
