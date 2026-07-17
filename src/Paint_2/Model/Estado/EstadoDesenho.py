from abc import ABC, abstractmethod


# ==========================
# Classe abstrata dos estados
# ==========================

class EstadoDesenho(ABC):
    """
    Classe abstrata que representa um estado do ciclo de desenho.

    Responsabilidade: definir a interface obrigatória que todo estado
    concreto do Controller deve implementar, permitindo que o
    comportamento dos eventos de mouse (clique, arrasto e soltura)
    varie de acordo com a etapa atual do desenho.

    Uso: cada estado concreto decide, para cada método, se a ação é
    permitida e qual a transição de estado resultante, delegando as
    chamadas de fato para a figura/model/view através do ``controller``.
    @author Jorge
    @version 1.0
    @see EstadoOcioso
    @see EstadoDesenhando
    """

    @abstractmethod
    def iniciar(self, controller, event):
        """
        Trata o evento de clique inicial do mouse (ButtonPress).

        @param controller instância do Controller (contexto), usada para
        acessar a figura atual, o model e a view
        @param event evento de clique do mouse (tkinter.Event)
        """
        pass

    @abstractmethod
    def atualizar(self, controller, event):
        """
        Trata o evento de arrasto do mouse (B1-Motion).

        @param controller instância do Controller (contexto)
        @param event evento de movimento do mouse (tkinter.Event)
        """
        pass

    @abstractmethod
    def incluir(self, controller, event):
        """
        Trata o evento de soltura do botão do mouse (ButtonRelease).

        @param controller instância do Controller (contexto)
        @param event evento de soltura do mouse (tkinter.Event)
        """
        pass