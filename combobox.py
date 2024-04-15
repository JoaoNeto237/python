from tkinter.ttk import *
from tkinter import *


janela = Tk()
janela.geometry('300x250')
janela.title("Combobox")

lb_nome = Label(janela, width=15, height=2, text="Faça a sua escolha", font=("Arial 10"), anchor='w')
lb_nome.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

#Funcao para obter os resultados da Combobox
def obter():
    resultado = combo.get()
    print(resultado)

#Criando a combobox
combo = Combobox(janela)
#Definindo valores para a combobox. 
combo['values'] = (1,2,3,4)
combo.current(0)


#Posicionando a Combobox na janela
combo.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)




botao = Button(janela,command=obter, text='Ver resposta', width=10, relief='raised', bg='white')
botao.grid(row=2, column=0, padx=5, pady=20)






janela.mainloop()