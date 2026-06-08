from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Computador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('NOTEBOOK', 'Notebook'), ('PC_GAMER', 'PC Gamer'), ('MONITOR', 'Monitor'), ('TECLADO', 'Teclado'), ('MOUSE', 'Mouse'), ('ACESSORIO', 'Acessório')], max_length=20)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.PositiveIntegerField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('disponivel', models.BooleanField(default=True)),
            ],
        ),
    ]
