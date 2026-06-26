from src.Paint_2.Model.Figuras import Figuras
import math

class Poligono(Figuras):
    """
    Representar um polígono desenhado na tela.
            
    Esta classe herda de ``Figuras`` e é responsável por armazenar
    as informações necessárias para criar e atualizar uma figura
    durante o desenho realizado pelo usuário.
            
            
    atributos:
        cor_borda(str): cor da borda
        cor_preenchimento(str): cor de preenchiemnto
        lados(int): números de lados 
    """

    def __init__(
        self,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados = 3,
    ):
        super().__init__(
            cor_borda,
            cor_preenchimento,
            lados
            )
            

    def calcular_vertices(self, coords):
        """
        Calcula as coordenadas dos vértices de um polígono regular.
        """
        x1, y1, x2, y2 = coords
        centro_x = (x1 + x2) / 2
        centro_y = (y1 + y2) / 2
        raio_x = abs(x2 - x1) / 2
        raio_y = abs(y2 - y1) / 2

        vertices = []
        for i in range(self.lados):
            angulo = 2 * math.pi * i / self.lados - math.pi / 2
            x = centro_x + raio_x * math.cos(angulo)
            y = centro_y + raio_y * math.sin(angulo)
            vertices.extend([x, y])
        return vertices


    def iniciar_figura(self, event):
        """
        define o ponto inicial da figura.
        """
        self.x_inicial = event.x
        self.y_inicial = event.y

    def atualizar_figura(self, event):
        """
        atualiza as dimenções da figura conforme o monvimento do mouse.
        """
        pontos = (self.x_inicial, self.y_inicial, event.x, event.y)
        vertices = self.calcular_vertices(pontos)

        self.figura_nova = (
            "poligono",
            vertices,
            self.cor_borda,
            self.cor_preenchimento,
        )


    def incompleta(self, figura):
        """
        retorna True para quando o tamanho da figura não for válido.
        """
        vertices = figura[1]
        return vertices[0] == vertices[2] and vertices[1] == vertices[3]