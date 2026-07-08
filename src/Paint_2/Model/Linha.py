from src.Paint_2.Model.Figuras import Figuras

class Linha(Figuras):
    """
    Representar uma linha desenhada na tela.
    
     Responsabilidade: armazenar a cor da borda 
    de uma linha, calculando suas dimensões conforme
    o movimento do mouse durante o desenho.

    Uso: instanciada pelo Controlador quando o usuário seleciona a
    ferramenta "Linha" e clica/arrasta no Canvas. Herda de
    ``Figuras`` o comportamento comum a todas as figuras do sistema
    
     atributos:
        cor_borda(str): cor da borda
         cor_preenchimento(str): cor de preenchiemnto
         lados(int): números de lados (mantidos por compatibilidade com a superclasse)
    @author Jorge
    @version 1.0
    @see Figuras
    """
    def __init__(
        self,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados = 3
        ):
        """
        Cria um nova linha com as cores informadas.

        O raio é inicializado como 0 e só é definido quando o usuário
        começa a desenhar (ver ``iniciar_figura`` e ``atualizar_figura``).

        @param cor_borda cor da borda da linha (padrão: "black")
        @param lados parâmetro mantido por compatibilidade com a superclasse;
        não possui efeito sobre a linha.
        """
        super().__init__(
            cor_borda,
            cor_preenchimento,
            lados
            )


    def iniciar_figura(self, event):
        """
        Define o ponto inicial da linha, a partir do clique do usuário.

        @param event evento de clique do mouse (tkinter.Event), contendo
        as coordenadas x e y de onde o desenho começou

        self.inic_x = event.x
        self.inic_y = event.y.
        """
        self.inic_x = event.x
        self.inic_y = event.y

        
    def atualizar_figura(self,event):
        """
        Atualiza  as coordenadas da linha conforme o
        movimento do mouse, recalculando a figura a cada chamada.

        @param event evento de movimento do mouse (tkinter.Event),
        @see iniciar_figura.
        """
        self.figura_nova = (
            "linha",
            (self.inic_x, self.inic_y, event.x, event.y),
            self.cor_borda,
            self.cor_preenchimento
            )
    
    def incompleta(self, event):
        """
        Verifica se a linha atual é inválido, ou seja, se o usuário
        clicou e soltou o mouse sem arrastar .

        @param event evento do mouse recebido no momento da verificação
               (não utilizado diretamente, mantido por compatibilidade
               com a assinatura da superclasse)
        @return True se o linha não possui tamanho válido (raio zero);
                False caso contrário
        """
        values = self.figura_nova[1]
        return (values[0], values[1]) == (values[2], values[3])
        