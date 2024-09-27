class Carrinho:
    def __init__(self, nome, cor, img_link):
        self.nome = nome
        self.cor = cor
        self.img_link = img_link

octane = Carrinho('octane', 'preto', 'https://static.wikia.nocookie.net/rocketleague/images/7/71/Octane_hero_art.jpg')
fennec = Carrinho('fennec', 'titanium white', 'https://static.wikia.nocookie.net/rocketleague/images/a/a6/Fennec_hero_art.jpg')

carrinhos = [octane, fennec]