from src.Paint_2.Model.Figuras import Figuras

class Borracha(Figuras):
    """
    Representa o rastro apagado pela ferramenta borracha.

    Responsabilidade: funcionar exatamente como uma LinhaLivre, porém
    desenhada com a cor de fundo do Canvas, cobrindo visualmente tudo
    que estiver embaixo do cursor conforme o usuário arrasta o mouse.
    A espessura do traço é ajustável, controlando a área apagada.

    Uso: instanciada pelo Controller quando o usuário seleciona a
    ferramenta "Borracha". Herda de ``Figuras`` o comportamento comum
    a todas as figuras do sistema.

    atributos:
        cor_borda(str): cor usada para "apagar" (igual ao fundo do Canvas)
        espessura(int): espessura do traço da borracha, em pixels
    @author Angel
    @version 1.0
    @see Figuras
    @see LinhaLivre
    """
    def __init__(
        self,
        cor_borda: str = 'white',
        cor_preenchimento: str = 'white',
        lados = 3,
        espessura: int = 10,
    ):
        """
        Cria uma nova borracha com a espessura informada.

        @param cor_borda cor usada para sobrepor o que for apagado
        (padrão: "white", igual ao fundo do Canvas)
        @param cor_preenchimento mantido por compatibilidade com a superclasse
        @param lados mantido por compatibilidade com a superclasse
        @param espessura espessura do traço da borracha, em pixels (padrão: 10)
        """
        super().__init__(
            cor_borda,
            cor_preenchimento,
            lados
        )
        self.espessura = espessura

    def iniciar_figura(self, event):
        """
        Define o ponto inicial do traço da borracha, a partir do clique do usuário.

        @param event evento de clique do mouse (tkinter.Event), contendo
        as coordenadas x e y de onde o traço começou
        """
        self.figura_nova = (
            "borracha",
            ([(event.x, event.y)]),
            self.cor_borda,
            self.espessura
        )

    def atualizar_figura(self, event):
        """
        Acrescenta o ponto atual do cursor ao traço da borracha conforme
        o movimento do mouse.

        @param event evento de movimento do mouse (tkinter.Event)
        @see iniciar_figura
        """
        self.figura_nova[1].append((event.x, event.y))

    def incompleta(self, figura):
        """
        Verifica se o traço da borracha é inválido, ou seja, se o usuário
        clicou e soltou o mouse sem arrastar.

        @param figura tupla contendo os dados do traço a ser validado
        @return True se o traço possui apenas um ponto (ou nenhum);
        False caso contrário
        """
        return len(figura[1]) <= 1