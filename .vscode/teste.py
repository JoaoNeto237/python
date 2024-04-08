from tkinter import *

def click():
    


janela = Tk()

lb = Label(janela, text="Meu nome é joão Cunha clique no botão para saber mais!")
lb.place(x=50,y=100)
bt = Button(janela, text="Clique em mim!")
bt.place(x=150, y=150)
lb1 = Label(janela, text="Meu pau é grande!")


janela.geometry("500x500")
janela.mainloop()