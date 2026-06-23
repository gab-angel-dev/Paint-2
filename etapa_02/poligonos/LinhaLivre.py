from poo.poligonos.Figuras import Figuras

class LinhaLivre(Figuras):
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
        self.pontos =[(x1,y2)]


    def iniciar_figura(self,x,y):
        self.pontos.append((x,y))
        


    def atualizar_figura(self,canvas,traco = False):
        if len(self.pontos) > 1:
            dash_param = (4, 2) if traco else None
            canvas.create_line(self.pontos, fill=self.cor_borda, dash=dash_param)
        
    
    def incluir_figura(self):
        pass
    
    def desenhar_figura(self):
        pass
    
    def desenhar_figura_nova(self):
        pass
    
    def incompleta(self):
        return len(self.pontos) <=1