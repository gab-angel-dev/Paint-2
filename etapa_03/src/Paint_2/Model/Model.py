class Model():
    def __init__(self):
        self.historico_figuras = []

    def adicionar_figura(self, figura):
        self.historico_figuras.append(figura)

    def get_figuras(self):
        return self.historico_figuras

    def limpar(self):
        self.historico_figuras = []