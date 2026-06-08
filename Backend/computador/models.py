from django.db import models


class Computador(models.Model):
    CATEGORIAS = [
        ('NOTEBOOK', 'Notebook'),
        ('PC_GAMER', 'PC Gamer'),
        ('MONITOR', 'Monitor'),
        ('TECLADO', 'Teclado'),
        ('MOUSE', 'Mouse'),
        ('ACESSORIO', 'Acessório'),
    ]

    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    estoque = models.PositiveIntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Produto(Computador):
    class Meta:
        proxy = True
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'