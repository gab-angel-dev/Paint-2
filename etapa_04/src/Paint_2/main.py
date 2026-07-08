# PROGRAMA PRINCIPAL

from etapa_03.src.Paint_2.Model.Linha import Linha
from etapa_03.src.Paint_2.Model.LinhaLivre import LinhaLivre
from etapa_03.src.Paint_2.Model.Oval import Oval
from etapa_03.src.Paint_2.Model.Circulo import Circulo
from etapa_03.src.Paint_2.Model.Retangulo import Retangulo
from etapa_03.src.Paint_2.Model.Poligono import Poligono

from etapa_03.src.Paint_2.Controller.Controller import Controller



figuras_classes = {
    "Linha": Linha,
    "Rabisco": LinhaLivre,
    "Retângulo": Retangulo,
    "Oval": Oval,
    "Círculo": Circulo,
    "Poligono": Poligono
}

cores = {
    "Preto": 'black',
    "Branco": 'white',
    "Amarelo": 'yellow',
    "Azul": 'blue',
    "Verde": 'green',
    "Vermelho": 'red',
    "Rosa": 'pink',
    "Cinza": 'gray'
}

def main():

    Controller(
       figuras=figuras_classes,
       cores=cores
    )
    


if __name__ == "__main__":
    main()