from etapa_02.poligonos.Figuras import Figuras
#from tkinter import *

#Todos os comentarios aqui são para a interface
#fiz para testar

class Linha(Figuras):
    def __init__(
        self,
        canvas,
        historico_figuras: list[tuple],
        nome = None,
        x1: int = 0,
        y1: int = 0,
        x2: int = 0,
        y2: int = 0,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados = 3
        ):
        super().__init__(
            nome,
            x1,
            y1,
            x2,
            y2,
            cor_borda,
            cor_preenchimento,
            lados
            )
        self.canvas = canvas
        self.historico_figuras = historico_figuras


    def iniciar_figura(self,event):
        self.figura_nova  = (
            "linha",
            (event.x, event.y, event.x, event.y),
            self.cor_borda,
            self.cor_preenchimento
        )

        
    def atualizar_figura(self,event):
        self.figura_nova = (
            "linha",
            (self.figura_nova[1][0], self.figura_nova[1][1], event.x, event.y),
            self.cor_borda,
            self.cor_preenchimento
            )
        
        self.desenhar_figura()
        self.desenhar_figura_nova()

    def desenhar_figura(self):
        return super().desenhar_figura()
        
    
    def desenhar_figura_nova(self):
        values = self.figura_nova[1]
        self.canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2))
        

    def incluir_figura(self,event):
        if not self.incompleta(self.figura_nova): 
            self.historico_figuras.append(self.figura_nova) 
        self.desenhar_figura()
    
    
    def incompleta(self, event):
        values = self.figura_nova[1]
        return (values[0], values[1]) == (values[2], values[3])
        