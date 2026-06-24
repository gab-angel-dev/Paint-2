from etapa_02.poligonos.Figuras import Figuras


class Retangulo(Figuras):
    def __init__(
        self,
        canvas,
        historico_figuras: list[tuple],
        nome= None,
        x1=0,
        y1=0,
        x2=0,
        y2=0,
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
        self.canvas = canvas
        self.historico_figuras = historico_figuras

    def iniciar_figura(self,event):
        self.figura_nova = (
            'retangulo', 
            (event.x, event.y,
            event.x, event.y),
            self.cor_borda, 
            self.cor_preenchimento
            )


    def atualizar_figura(self, event):
        self.figura_nova = (
            'retangulo',
            (self.figura_nova[1][0],
            self.figura_nova[1][1], 
            event.x, event.y), 
            self.cor_borda, 
            self.cor_preenchimento
        )
        self.desenhar_figura()
        self.desenhar_figura_nova()
        
    
    def incluir_figura(self,event):
        if not self.incompleta(self.figura_nova):
            self.historico_figuras.append(self.figura_nova)
        self.desenhar_figura()
    
    def desenhar_figura(self):
        return super().desenhar_figura()
        
    
    def desenhar_figura_nova(self):
        fig, values, cor_outline, cor_fill = self.figura_nova
        self.canvas.create_rectangle(
            values,
            dash=(4, 2),
            outline=cor_outline,
            fill=cor_fill ,
            width=2
            )
    
    def incompleta(self, event):
        values = self.figura_nova[1]
        return (values[0], values[1]) == (values[2], values[3])