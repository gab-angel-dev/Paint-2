from etapa_03.src.Paint_2.Model import Figuras

class LinhaLivre(Figuras):
    def __init__(
        self,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados =3 
        ):
        super().__init__(
            cor_borda,
            cor_preenchimento,
            lados
            )


    def iniciar_figura(self, event):
        self.figura_nova  = (
            "rabisco",
            ([(event.x, event.y)]),
            self.cor_borda,
            self.cor_preenchimento
        )

    def atualizar_figura(self, event):
        self.figura_nova[1].append((event.x, event.y))
    
    def incompleta(self):
        return len(self.figura_nova[1]) <=1