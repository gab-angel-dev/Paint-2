from poo.poligonos.Figuras import Figuras
#from tkinter import *

#Todos os comentarios aqui são para a interface
#fiz para testar

class Linha(Figuras):
    def __init__(
        self,
        nome,
        x1,
        y1,
        x2,
        y2,
        # canvas,
        cor_borda = 'black',
        cor_preenchimento = 'white',
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
        # self.canvas = canvas
        # self.ini_x = None
        # self.ini_y = None
        # self.fim_x = None
        # self.fim_y = None

        # self.canvas.bind('<ButtonPress-1>',self.iniciar_figura)
        # self.canvas.bind('<B1-Motion>',self.atualizar_figura)


    def iniciar_figura(self,event):
        self.ini_x = event.x
        self.ini_y = event.y
        return super().iniciar_figura()


    def atualizar_figura(self,event):
        self.fim_x = event.x
        self.fim_y = event.y
        self.canvas.delete("all")
        self.canvas.create_line(self.ini_x, self.ini_y, self.fim_x, self.fim_y)

        return super().atualizar_figura()
    
    def incluir_figura(self):
        return super().incluir_figura()
    
    def desenhar_figura(self):
        return super().desenhar_figura()
    
    def desenhar_figura_nova(self):
        return super().desenhar_figura_nova()
    
    def incompleta(self):
        return super().incompleta()


'''
#******MAIN*******#       
class AplicacaoPOO:
    def __init__(self, root):
        self.root = root
        self.root.title("Desenho em POO")
        
        # Configuração do Canvas
        self.canvas = Canvas(self.root, bg='white', width=600, height=600)
        self.canvas.pack()
        
        # Instancia a lógica de desenho passando o canvas desta janela
        self.ferramenta = Linha("Linha1", 0, 0, 0, 0, self.canvas)

# ******* MAIN ******* #
if __name__ == "__main__":
    root = Tk()
    app = AplicacaoPOO(root)
    root.mainloop()
'''