from src.Paint_2.Model.Estado.EstadoDesenho import EstadoDesenho


# ==========================
# Estado: Desenhando
# ==========================

class EstadoDesenhando(EstadoDesenho):
    """
    Representa o estado em que uma figura está sendo desenhada,
    ou seja, entre o clique inicial e a soltura do mouse.

    Responsabilidade: atualizar a figura em tempo real durante o
    arrasto, e finalizar/registrar a figura no model ao soltar o
    mouse, retornando o Controller ao estado ``EstadoOcioso``.
    @author Jorge
    @version 1.0
    @see EstadoOcioso
    """

    def iniciar(self, controller, event):
        """
        Ignora um novo clique: já existe uma figura em desenho.

        @param controller instância do Controller (contexto)
        @param event evento de clique do mouse (tkinter.Event)
        """
        print("Erro: já existe uma figura sendo desenhada.")

    def atualizar(self, controller, event):
        """
        Atualiza a figura corrente conforme o arrasto do mouse e
        solicita à view o redesenho do Canvas.

        @param controller instância do Controller (contexto)
        @param event evento de movimento do mouse (tkinter.Event)
        """
        controller.figura_atual.atualizar_figura(event)
        figuras = controller.model.get_figuras()
        controller.view.redesenhar(figuras, controller.figura_atual.figura_nova)

    def incluir(self, controller, event):
        """
        Finaliza o desenho da figura ao soltar o clique do mouse.

        Valida se a figura possui dimensões válidas e, se correto,
        solicita ao model a sua inclusão definitiva no histórico.
        Em seguida, retorna o Controller para o estado ``EstadoOcioso``.

        @param controller instância do Controller (contexto)
        @param event evento de soltura do mouse (tkinter.Event)
        """
        if not controller.figura_atual.incompleta(controller.figura_atual.figura_nova):
            controller.model.adicionar_figura(controller.figura_atual.figura_nova)
        controller.view.redesenhar(controller.model.get_figuras())

        from src.Paint_2.Model.Estado.EstadoOcioso import EstadoOcioso
        controller.estado = EstadoOcioso()