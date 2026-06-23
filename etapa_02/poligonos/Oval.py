from poo.poligonos.Figuras import Figuras


class Oval(Figuras):
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
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def iniciar_figura(self,x,y):
        self.x2 = x1
        self.y2 = y1

    def atualizar_figura(self):
        self.x2 = x 
        self.y2 = y

    def incluir_figura(self):
        pass
    
    def desenhar_figura(self,canvas,traco=False):
        dash_para = (4,2) if traco else None

        canvas.create_oval(self.x1, self.y1, self.x2, self.y2,
            outline=self.cor_borda, 
            fill=self.cor_preenchimento, 
            dash=dash_para 
            )
    
    def desenhar_figura_nova(self):
        pass
    
    def incompleta(self):
        return ((self.x1 == self.x2 and self.y1 == self.y2))