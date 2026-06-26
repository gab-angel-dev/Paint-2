from src.Paint_2.Model.Figuras import Figuras



class Circulo(Figuras):
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
        
        self.raio = 0 


    def iniciar_figura(self, event):
        self.inic_x = event.x
        self.inic_y = event.y

    def atualizar_figura(self, event):
        self.raio = min(
        abs(event.x-self.inic_x),
        abs(event.y-self.inic_y)
        )
        self.figura_nova = (
            'circulo', 
            (self.inic_x, self.inic_y, self.inic_x +self.raio, self.inic_y +self.raio),
            self.cor_borda,
            self.cor_preenchimento
            )

      
    def incompleta(self, event):
        values = self.figura_nova[1]
        return (values[0], values[1]) == (values[2], values[3])