from tkinter import *

def btclick():
    if(str(en.get()).isnumeric() and str(en2.get()).isnumeric()):
        num1 = int(en.get())
        num2 = int(en2.get())

        lb["text"] = num1 + num2
    else:
        lb["text"] = "Valores informados invalidos"
        
janela = Tk()
janela.title("Calculadora")
lb1 = Label(janela, text="Some Valores!")
lb1.place(x=100 ,y=50)

en = Entry(janela)
en.place(x=100, y=100)

en2 = Entry(janela)
en2.place(x=100, y=150)

bt = Button(janela, width=20, text="SOMAR", command= btclick)
bt.place(x=100, y=200)

lb = Label(janela, text=("Resultado"))
lb.place(x=100, y=250)

janela.geometry("300x300")
janela.mainloop()
