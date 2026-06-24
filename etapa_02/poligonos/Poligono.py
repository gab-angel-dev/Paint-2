from etapa_02.poligonos.Figuras import Figuras
import math

class Poligono(Figuras):
    def __init__(
        self,
        nome,
        x1,
        y1,
        x2,
        y2,
        lados,
        cor_borda = 'black',
        cor_preenchimento = 'white'
        ):
        super().__init__(
            nome,
            x1,
            y1,
            x2,
            y2,
            cor_borda,
            cor_preenchimento
            )
        # Garante que o polígono possua no mínimo 3 lados
        self.lados = max(3, lados)

    def iniciar_figura(self,x,y):
        # Define o ponto inicial do desenho.
        self.x1 = x 
        self.y1 = y
        self.x2 = x 
        self.y2 = y 
        

    def atualizar_figura(self,x,y):
        # atualiza conforme arrasta o mouse pela tela
        self.x2 = x 
        self.y2 = y
        
    def calcular_vertices(self):
        #Calcula o centro do retângulo delimitador.
        centro_x = (self.x1 + self.x2) / 2
        centro_y = (self.y1 + self.y2) / 2

        #Calcula o centro do retângulo delimitador.
        raio_x = abs(self.x2 - self.x1) / 2
        raio_y = abs(self.y2 - self.y1) / 2

        #Lista que armazenará todos os vértices
        vertices = []

        # Calcula cada vértice do polígono regular
        for i in range(self.lados):

            # Divide a circunferência em partes iguais.
            # triângulo = 120°, quadrado = 90°, pentágono = 72°
            angulo = 2 * math.pi * i / self.lados - math.pi / 2

            x = centro_x + raio_x * math.cos(angulo)
            y = centro_y + raio_y * math.sin(angulo)

            # Adiciona o vértice calculado à lista
            vertices.extend([x, y])

        return vertices

    def incluir_figura(self):
        pass
    
    def desenhar_figura(self,canvas,traco=False):
        dash_para = (4, 2) if traco else None

        # Desenha o polígono utilizando os vértices
        canvas.create_polygon(
            self.calcular_vertices(),
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
            dash=dash_para
        )
        
    def desenhar_figura_nova(self):
        pass
        
    
    def incompleta(self):
         # A figura é considerada incompleta quando
        # o ponto inicial e final possuem as mesmas coordenadas.
        return (
            self.x1 == self.x2 and
            self.y1 == self.y2
        )