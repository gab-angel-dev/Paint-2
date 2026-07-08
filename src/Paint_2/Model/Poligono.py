from src.Paint_2.Model.Figuras import Figuras
import math

class Poligono(Figuras):
    """
    Representar um polígono desenhado na tela.
            
    Responsabilidade: armazenar o tamanho, a cor da borda e a cor de
    preenchimento de um Poligono, calculando suas dimensões conforme
    o movimento do mouse durante o desenho.
        
    Uso: instanciada pelo Controlador quando o usuário seleciona a
    ferramenta "Poligono" e seleciona a quantidade de lados,
    clica/arrasta no Canvas. Herda de``Figuras`` o comportamento
    comum a todas as figuras do sistema.
            
    atributos:
        cor_borda(str): cor da borda
        cor_preenchimento(str): cor de preenchiemnto
        lados(int): números de lados
    @author Jorge
    @version 1.0
    @see figuras
    """

    def __init__(
        self,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados = 3,
    ):
        """
        Cria  um novo poligono com as cores informadas.
                
        O raio é inicializado como 0 e só é definido quando o usuário
        começa a desenhar (ver ``iniciar_figura`` e ``atualizar_figura``).
                
        @param cor_borda cor da borda de um Poligono (padrão: "black")
        @param cor_preenchimento cor de preenchimento do Poligono (padrão: "white")
        @param lados parâmetro mantido por compatibilidade com a superclasse;
        possui efeito sobre o Poligono
        """
        super().__init__(
            cor_borda,
            cor_preenchimento,
            lados
            )
            

    def calcular_vertices(self, coords):
        """
        Calcula as coordenadas dos vértices de um polígono regular.
        
        A partir das coordenadas da diagonal da área de desenho, determina
        o centro e os raios nos eixos X e Y para distribuir os vértices
        de forma equidistante com base no número de lados.
        
        @param coords tupla ou lista contendo (x1, y1, x2, y2) que define
        a área de delimitação do polígono
        @return lista com as coordenadas [x, y, x, y, ...] de todos os 
        vértices do polígono regular
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
        Define o ponto inicial do Poligono, a partir do clique do usuário.
        @param event evento de clique do mouse (tkinter.Event), contendo
        as coordenadas x e y de onde o desenho começou.
        """
        self.x_inicial = event.x
        self.y_inicial = event.y

    def atualizar_figura(self, event):
        """
        Atualiza  as coordenadas do Poligono conforme o
        movimento do mouse, recalculando a figura a cada chamada.
        @param event evento de movimento do mouse (tkinter.Event),
        contendo a posição atual usada para recalcular o raio
        @see iniciar_figura
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
        Verifica se o retangulo atual é inválido, ou seja, se o usuário
        clicou e soltou o mouse sem arrastar (raio igual a zero).
        @param event evento do mouse recebido no momento da verificação
        (não utilizado diretamente, mantido por compatibilidade
        com a assinatura da superclasse)
        @return True se o Oval não possui tamanho válido (raio zero);
        False caso contrário..
        """
        vertices = figura[1]
        return vertices[0] == vertices[2] and vertices[1] == vertices[3]