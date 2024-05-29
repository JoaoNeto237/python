from tkinter import *

root = Tk()

class Application:
    def __init__(self) -> None:
        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')

Application()

