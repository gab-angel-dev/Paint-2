from etapa_03.src.Paint_2.Model.Figuras import Figuras



class Circulo(Figuras):
    def __init__(
        self,
        canvas,
        historico_figuras,
        x1: int = 0,
        y1: int = 0,
        x2: int = 0,
        y2: int = 0,
        nome = None,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados = 3
        ):
        super().__init__(
            canvas,
            historico_figuras,
            x1,
            y1,
            x2,
            y2,
            nome,
            cor_borda,
            cor_preenchimento,
            lados
            )
        self.raio = 0 


    def iniciar_figura(self, event):
        self.figura_nova  = (
            "circulo",
            (event.x, event.y, event.x, event.y),
            self.cor_borda,
            self.cor_preenchimento
        )

    def atualizar_figura(self, event):
        self.raio = min(
        abs(event.x-self.figura_nova[1][0]),
        abs(event.y-self.figura_nova[1][1])
        )
        self.figura_nova = (
            'circulo', 
            (self.figura_nova[1][0], self.figura_nova[1][1], self.figura_nova[1][0]+self.raio, self.figura_nova[1][1]+self.raio),
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
        self.canvas.create_oval(
            values,
            dash=(4, 2),
            outline=cor_outline,
            fill=cor_fill,
            width=2
            )
        
    
    def incompleta(self, event):
        values = self.figura_nova[1]
        return (values[0], values[1]) == (values[2], values[3])