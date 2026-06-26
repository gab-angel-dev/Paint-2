from src.Paint_2.Model.Figuras import Figuras
import math

class Poligono(Figuras):
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
        self.x_inicial = event.x
        self.y_inicial = event.y

    def atualizar_figura(self, event):
        pontos = (self.x_inicial, self.y_inicial, event.x, event.y)
        vertices = self.calcular_vertices(pontos)

        self.figura_nova = (
            "poligono",
            vertices,
            self.cor_borda,
            self.cor_preenchimento,
        )


    def incompleta(self, figura):
        vertices = figura[1]
        return vertices[0] == vertices[2] and vertices[1] == vertices[3]