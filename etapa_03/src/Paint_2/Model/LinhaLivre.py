from etapa_02.poligonos.Figuras import Figuras

class LinhaLivre(Figuras):
    def __init__(
        self,
        canvas,
        historico_figuras: list[tuple],
        nome = None,
        x1=0,
        y1=0,
        x2=0,
        y2=0,
        cor_borda = 'black',
        cor_preenchimento = 'white',
        lados =3 
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


    def iniciar_figura(self, event):
        self.figura_nova  = (
            "rabisco",
            ([(event.x, event.y)]),
            self.cor_borda,
            self.cor_preenchimento
        )

    def atualizar_figura(self, event):
        self.figura_nova[1].append((event.x, event.y))
        self.desenhar_figura()
        self.desenhar_figura_nova()
    
    def incluir_figura(self,event):
        if not self.incompleta(): 
            self.historico_figuras.append(self.figura_nova)
        self.desenhar_figura() 
        
    
    def desenhar_figura(self):
        return super().desenhar_figura()        
    
    def desenhar_figura_nova(self):
        tipo, values, cor_outline, cor_fill = self.figura_nova
        self.canvas.create_line(values, dash=(4, 2))
    
    def incompleta(self):
        return len(self.figura_nova[1]) <=1