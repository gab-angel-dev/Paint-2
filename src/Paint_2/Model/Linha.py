from src.Paint_2.Model.Figuras import Figuras

class Linha(Figuras):
    def __init__(
        self,
        cor_borda: str = 'black',
        cor_preenchimento: str = 'white',
        lados = 3
        ):
        super().__init__(
            cor_borda,
            cor_preenchimento,
            lados
            )


    def iniciar_figura(self, event):
        self.inic_x = event.x
        self.inic_y = event.y

        
    def atualizar_figura(self,event):
        self.figura_nova = (
            "linha",
            (self.inic_x, self.inic_y, event.x, event.y),
            self.cor_borda,
            self.cor_preenchimento
            )
    
    def incompleta(self, event):
        values = self.figura_nova[1]
        return (values[0], values[1]) == (values[2], values[3])
        