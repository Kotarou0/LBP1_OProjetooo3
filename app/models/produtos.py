class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

LISTA_PRODUTOS = [
    Produto(1, 'Abacaxi', 5),
    Produto(2, 'Banana', 3),
    Produto(3, 'Canela', 7)
]
