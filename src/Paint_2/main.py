# PROGRAMA PRINCIPAL

from src.Paint_2.Model.Linha import Linha
from src.Paint_2.Model.LinhaLivre import LinhaLivre
from src.Paint_2.Model.Oval import Oval
from src.Paint_2.Model.Circulo import Circulo
from src.Paint_2.Model.Retangulo import Retangulo
from src.Paint_2.Model.Poligono import Poligono

from src.Paint_2.Controller.Controller import Controller



figuras_classes = {
    "Linha": Linha,
    "Rabisco": LinhaLivre,
    "Retângulo": Retangulo,
    "Oval": Oval,
    "Círculo": Circulo,
    "Poligono": Poligono
}

def main():

    Controller(
       figuras=figuras_classes
    )
    


if __name__ == "__main__":
    main()