from src.Paint_2.Model.Estado.EstadoDesenho import EstadoDesenho


# ==========================
# Estado: Ocioso
# ==========================

class EstadoOcioso(EstadoDesenho):
    """
    Representa o estado em que nenhuma figura está sendo desenhada.

    Responsabilidade: aceitar o clique inicial do mouse para começar
    uma nova figura, e ignorar eventos de arrasto ou soltura que
    cheguem fora de ordem (sem um clique inicial prévio).
    @author Jorge
    @version 1.0
    @see EstadoDesenhando
    """

    def iniciar(self, controller, event):
        """
        Inicia uma nova figura a partir do clique do usuário e
        transiciona o Controller para o estado ``EstadoDesenhando``.

        @param controller instância do Controller (contexto)
        @param event evento de clique do mouse (tkinter.Event)
        """
        if controller.figura_atual:
            controller.figura_atual.iniciar_figura(event)

            from src.Paint_2.Model.Estado.EstadoDesenhando import EstadoDesenhando
            controller.estado = EstadoDesenhando()

    def atualizar(self, controller, event):
        """
        Ignora o arrasto do mouse: não há figura em desenho.

        @param controller instância do Controller (contexto)
        @param event evento de movimento do mouse (tkinter.Event)
        """
        pass

    def incluir(self, controller, event):
        """
        Ignora a soltura do mouse: não há figura em desenho.

        @param controller instância do Controller (contexto)
        @param event evento de soltura do mouse (tkinter.Event)
        """
        pass