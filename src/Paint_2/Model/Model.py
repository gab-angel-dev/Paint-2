import pickle


class Model():
    """
    Representa o modelo da aplicação.

    Esta classe é responsável por armazenar e gerenciar o histórico
    das figuras desenhadas, disponibilizando operações para adicionar,
    consultar, remover e persistir figuras.
    
    atributos:
        historico_figuras(list): lista que armazena todas as figuras desenhadas
    @author Jorge
    @version 1.0.
    """
    def __init__(self):
        """
        Inicializa o modelo com um histórico de figuras vazio.
        """
        self.historico_figuras = []

    def adicionar_figura(self, figura):
        """
        Adiciona uma nova figura ao histórico da aplicação.
        
        @param figura tupla contendo as propriedades e coordenadas da 
        figura a ser armazenada (ex: tipo, vértices, cor de borda, preenchimento)
        """
        self.historico_figuras.append(figura)

    def get_figuras(self):
        """
        Retorna a lista completa de figuras atualmente armazenadas.
        
        @return list contendo todas as figuras presentes no histórico
        """
        return self.historico_figuras

    def limpar(self):
        """
        Remove todas as figuras do histórico, limpando a tela da aplicação.
        """
        self.historico_figuras = []

    def salvar_arquivo(self, caminho):
        """
        Serializa e persiste o histórico de figuras em um arquivo binário.
        
        @param caminho caminho completo ou nome do arquivo onde os dados 
        serão salvos (utilizando a biblioteca pickle)
        """
        with open(caminho, 'wb') as arquivo:
            pickle.dump(self.historico_figuras, arquivo)

    def abrir_arquivo(self, caminho):
        """
        Carrega e desserializa o histórico de figuras a partir de um arquivo binário.
        
        @param caminho caminho completo ou nome do arquivo de onde os dados 
        serão lidos (utilizando a biblioteca pickle)
        """
        with open(caminho, 'rb') as arquivo:
            self.historico_figuras = pickle.load(arquivo)