from tkinter import *

janela = Tk()
janela.title('Radiobutton')
janela.geometry('300x250')

#Obter os valores do Radiobutton
def obter():
    resp = selecionado_1.get()
    print(resp)

#Variaveis que serao usadas para obter os valores
selecionado_1 = IntVar()
selecionado_2 = BooleanVar()
selecionado_3 = StringVar()

#Criando o Radiobutton
radio = Radiobutton(janela, text='Primeiro', command=obter ,value=10, variable=selecionado_1)
radio.grid(row=0, column=0, padx=10, pady=10)

radio2 = Radiobutton(janela, text='Segundo', command=obter ,value=20,variable=selecionado_1)
radio2.grid(row=1, column=0, padx=10, pady=10)

radio3 = Radiobutton(janela, text='Terceiro', command=obter ,value=30,variable=selecionado_1)
radio3.grid(row=3, column=0, padx=10, pady=10)


janela.mainloop()