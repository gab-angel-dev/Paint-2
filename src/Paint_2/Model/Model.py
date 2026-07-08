import pickle


class Model():
    """
    Representa o modelo da aplicação.

    Esta classe é responsável por armazenar e gerenciar o histórico
    das figuras desenhadas, disponibilizando operações para adicionar,
    consultar, remover e persistir figuras.
    """
    def __init__(self):
        self.historico_figuras = []

    def adicionar_figura(self, figura):
        self.historico_figuras.append(figura)

    def get_figuras(self):
        return self.historico_figuras

    def limpar(self):
        self.historico_figuras = []

    def salvar_arquivo(self, caminho):
        with open(caminho, 'wb') as arquivo:
            pickle.dump(self.historico_figuras, arquivo)

    def abrir_arquivo(self, caminho):
        with open(caminho, 'rb') as arquivo:
            self.historico_figuras = pickle.load(arquivo)