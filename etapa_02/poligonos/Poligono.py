from etapa_02.poligonos.Figuras import Figuras
import math

class Poligono(Figuras):
    def __init__(
        self,
        canvas,
        historico_figuras: list[tuple],
        lados: int = 3,
        nome=None,
        x1: int = 0,
        y1: int = 0,
        x2: int = 0,
        y2: int = 0,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
    ):
        super().__init__(
            nome,
            x1,
            y1,
            x2,
            y2,
            cor_borda,
            cor_preenchimento)
            
        self.canvas = canvas
        self.historico_figuras = historico_figuras
        self.lados = max(3, lados)

    def iniciar_figura(self, event):
        self.figura_nova = (
            "poligono",
            (event.x, event.y, event.x, event.y),
            self.cor_borda,
            self.cor_preenchimento,
            self.lados
        )

    def atualizar_figura(self, event):
        self.figura_nova = (
            "poligono",
            (self.figura_nova[1][0], self.figura_nova[1][1], event.x, event.y),
            self.cor_borda,
            self.cor_preenchimento,
            self.lados
        )
        self.desenhar_figura()
        self.desenhar_figura_nova()

    def incluir_figura(self, event):
        if not self.incompleta(self.figura_nova):
            self.historico_figuras.append(self.figura_nova)
        self.desenhar_figura()

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

    def desenhar_figura(self):
        return super().desenhar_figura()

    def desenhar_figura_nova(self):
        coords = self.figura_nova[1]
        lados = self.figura_nova[4]
        vertices = self.calcular_vertices(coords)
        self.canvas.create_polygon(
            vertices,
            outline=self.cor_borda,
            fill='',
            dash=(4, 2)
        )

    def incompleta(self, figura):
        values = figura[1]
        return (values[0], values[1]) == (values[2], values[3])