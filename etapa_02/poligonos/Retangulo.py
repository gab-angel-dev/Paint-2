from poo.poligonos.Figuras import Figuras


class Retangulo(Figuras):
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


    def iniciar_figura(self,mouse_x,mouse_y):
        self.x1 = mouse_x
        self.y1 = mouse_y
        self.x2 = mouse_x
        self.y2 = mouse_y


    def atualizar_figura(self, mouse_x, mouse_y):
        self.x2 = mouse_x
        self.y2 = mouse_y
        
    
    def incluir_figura(self):
        pass
    
    def desenhar_figura(self,canvas,traco=False):
        # Define se a linha do contorno será traco ou contínua
        dash_para = (4,2) if traco else None
        canvas.create_rectangle(
            self.x1,
            self.y1, 
            self.x2, 
            self.y2,
            outline=self.cor_borda, 
            fill=self.cor_preenchimento, 
            dash=dash_para
            )
        
    
    def desenhar_figura_nova(self):
        pass
    
    def incompleta(self):
        return ((self.x1, self.y1) == (self.x2, self.y2))