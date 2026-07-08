from src.Paint_2.Model.Figuras import Figuras



class Circulo(Figuras):
    """
    Representar um circulo desenhado na tela.

    Responsabilidade: armazenar o raio, a cor da borda e a cor de
    preenchimento de um círculo, calculando suas dimensões conforme
    o movimento do mouse durante o desenho.

    Uso: instanciada pelo Controlador quando o usuário seleciona a
    ferramenta "Círculo" e clica/arrasta no Canvas. Herda de
    ``Figuras`` o comportamento comum a todas as figuras do sistema.

    atributos:
        raio(int): raio atual do circulo
        cor_borda(str): cor da borda
        cor_preenchimento(str): cor de preenchiemnto
        lados(int): números de lados (mantidos por compatibilidade com a superclasse)

   @author Jorge
    @version 1.0
    @see figuras
    """
    def __init__(
        self,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados = 3
        ):
        """
        Cria  um novo círculo com as cores informadas.

        O raio é inicializado como 0 e só é definido quando o usuário
        começa a desenhar (ver ``iniciar_figura`` e ``atualizar_figura``).

        @param cor_borda cor da borda do círculo (padrão: "black")
        @param cor_preenchimento cor de preenchimento do círculo (padrão: "white")
        @param lados parâmetro mantido por compatibilidade com a superclasse;
               não possui efeito sobre o círculo
        """
        super().__init__(
            cor_borda,
            cor_preenchimento,
            lados
            )
        
        self.raio = 0 


    def iniciar_figura(self, event):
        """
        Define o ponto inicial do círculo, a partir do clique do usuário.
        @param event evento de clique do mouse (tkinter.Event), contendo
        as coordenadas x e y de onde o desenho começou
        """
        self.inic_x = event.x
        self.inic_y = event.y

    def atualizar_figura(self, event):
        """
        Atualiza o raio e as coordenadas do círculo conforme o
        movimento do mouse, recalculando a figura a cada chamada.
        @param event evento de movimento do mouse (tkinter.Event),
        contendo a posição atual usada para recalcular o raio
        @see iniciar_figura
        """
        self.raio = min(
        abs(event.x-self.inic_x),
        abs(event.y-self.inic_y)
        )
        self.figura_nova = (
            'circulo', 
            (self.inic_x, self.inic_y, self.inic_x +self.raio, self.inic_y +self.raio),
            self.cor_borda,
            self.cor_preenchimento
            )

      
    def incompleta(self, event):
        """
        Verifica se o círculo atual é inválido, ou seja, se o usuário
        clicou e soltou o mouse sem arrastar (raio igual a zero).
        @param event evento do mouse recebido no momento da verificação
        (não utilizado diretamente, mantido por compatibilidade
        com a assinatura da superclasse)
        @return True se o círculo não possui tamanho válido (raio zero);
        False caso contrário.
        """
        values = self.figura_nova[1]
        return (values[0], values[1]) == (values[2], values[3])
    