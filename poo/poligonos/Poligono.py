from poo.poligonos.Figuras import Figuras


class Poligono(Figuras):
    def __init__(
        self,
        nome,
        x1,
        y1,
        x2,
        y2,
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


    def iniciar_figura(self):
        return super().iniciar_figura()


    def atualizar_figura(self):
        return super().atualizar_figura()
    
    def incluir_figura(self):
        return super().incluir_figura()
    
    def desenhar_figura(self):
        return super().desenhar_figura()
    
    def desenhar_figura_nova(self):
        return super().desenhar_figura_nova()
    
    def incompleta(self):
        return super().incompleta()