from tkinter import *

janela = Tk()
janela.title('Cadastro')
janela["bg"] = 'gray'

#Funcao----------------------
def obter():
    nomee = nome.get()
    idadee = idade.get()
    paiss = pais.get()

    nome_re['text'] = nomee
    idade_re['text'] = idadee
    pais_re['text'] = paiss

    nome.delete(0, END)
    idade.delete(0, END)
    pais.delete(0, END)
#Campo de Label--------------

nome_lab = Label(janela, text="Nome:",width=15, font=('Arial 10'), anchor=W, fg='black')
nome_lab.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

idade_lab = Label(janela, text="Idade:",width=15, font=('Arial 10'), anchor=W, fg='black')
idade_lab.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)

pais_lab = Label(janela, text="Pais:",width=15, font=('Arial 10'), anchor=W, fg='black')
pais_lab.grid(row=2, column=0, padx=10, pady=5, sticky=NSEW)

#Campo de Entrada--------------

nome = Entry(janela, width=15,  font=('Arial 10'), fg='black')
nome.grid(row=0, column=1, padx=10, pady=5, sticky=W)

idade = Entry(janela, width=15,  font=('Arial 10'), fg='black')
idade.grid(row=1, column=1, padx=10, pady=5)

pais = Entry(janela, width=15,  font=('Arial 10'), fg='black')
pais.grid(row=2, column=1, padx=10, pady=5)

#Respostas---------------

nome_re = Label(janela, text="",width=15, font=('Arial 10'), anchor=W, fg='black')
nome_re.grid(row=0, column=2, padx=5, pady=5, sticky=NSEW)

idade_re = Label(janela, text="",width=15, font=('Arial 10'), anchor=W, fg='black')
idade_re.grid(row=1, column=2, padx=5, pady=5, sticky=NSEW)

pais_re = Label(janela, text="",width=15, font=('Arial 10'), anchor=W, fg='black')
pais_re.grid(row=2, column=2, padx=5, pady=5, sticky=NSEW)

#Botao------------------
botao = Button(janela, text='Ver dados', width=8, command=obter, relief=RAISED, fg='black')
botao.grid(row=3, column=0, padx=5, pady=5)

janela.geometry("500x200")
janela.mainloop()