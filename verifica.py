from tkinter import *
from datetime import time
import datetime

class Application:
    from datetime import date
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "8")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.place(x = 80, y = 0)

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 2
        self.segundoContainer["pady"] = 5
        self.segundoContainer.place(x = 10, y = 42)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 2
        self.terceiroContainer["pady"] = 5
        self.terceiroContainer.place(x = 10, y = 84)

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 2
        self.quartoContainer["pady"] = 5
        self.quartoContainer.place(x = 10, y = 126)

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 6
        self.quintoContainer["padx"] = 2
        self.quintoContainer.place(x = 10, y = 168)

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 6
        self.sextoContainer["padx"] = 2
        self.sextoContainer.place(x = 10, y = 210)

        self.setimoContainer = Frame(master)
        self.setimoContainer["pady"] = 6
        self.setimoContainer["padx"] = 2
        self.setimoContainer.place(x = 10, y = 252)

        self.titulo = Label(self.primeiroContainer, text="Cadastro")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack(side=LEFT)

        self.nomeLabel = Label(self.segundoContainer, text="Nome:",
        font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.terceiroContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.dataLabel = Label(self.quartoContainer, text="Data de Nascimento (DD/MM/AA):",
        font=self.fontePadrao)
        self.dataLabel.pack(side=LEFT)

        self.data = Entry(self.quintoContainer)
        self.data["width"] = 30
        self.data["font"] = self.fontePadrao
        self.data.pack(side=LEFT)

        self.enviar = Button(self.sextoContainer)
        self.enviar["text"] = "Enviar"
        self.enviar["font"] = self.fontePadrao
        self.enviar["width"]= 30
        self.enviar["command"] = self.autenticar
        self.enviar.pack()

        self.respostaLabel = Label(self.setimoContainer, text="", font=self.fontePadrao)
        self.respostaLabel.pack(side=LEFT)

    def autenticar(self):
        pnome = self.nome.get()
        pdata = self.data.get()
        tamanho = len(pdata)
        dataatual = datetime.datetime.now()

        if(tamanho == 10):
            nascdia = int(pdata[:2])
            nascmes = int(pdata[3:5])
            nascano = int(pdata[6:10])

            mesatt = int(dataatual.month)
            anoatt = int(dataatual.year)
            diaatt = int(dataatual.day)

            contano = anoatt - nascano
            
            if contano > 17:
                self.respostaLabel["text"] = f"{pnome} você é maior de idade !!!!"
            if contano == 17:
                self.respostaLabel["text"] = f"{pnome} você é maior de idade !!!!"
                if nascmes > mesatt:
                    self.respostaLabel["text"] = f"{pnome} você é maior de idade !!!!"
                if nascmes == mesatt:
                    if nascdia <= diaatt:
                        self.respostaLabel["text"] = f"{pnome} você é maior de idade !!!!"
                    else:
                        self.respostaLabel["text"] = f"{pnome} você não tem idade suficiente !!!!"
            if contano < 17:
                self.respostaLabel["text"] = f"{pnome} você não tem idade suficiente !!!!"
        if(tamanho == 8):
            nascdia = int(pdata[:2])
            nascmes = int(pdata[2:4])
            nascano = int(pdata[4:8])

            mesatt = int(dataatual.month)
            anoatt = int(dataatual.year)
            diaatt = int(dataatual.day)

            contano = anoatt - nascano
            
            if contano > 17:
                self.respostaLabel["text"] = f"{pnome} você é maior de idade !!!!"
            if contano == 17:
                self.respostaLabel["text"] = f"{pnome} você é maior de idade !!!!"
                if nascmes > mesatt:
                    self.respostaLabel["text"] = f"{pnome} você é maior de idade !!!!"
                if nascmes == mesatt:
                    if nascdia <= diaatt:
                        self.respostaLabel["text"] = f"{pnome} você é maior de idade !!!!"
                    else:
                        self.respostaLabel["text"] = f"{pnome} você não tem idade suficiente !!!!"
            if contano < 17:
                self.respostaLabel["text"] = f"{pnome} você não tem idade suficiente !!!!"
root = Tk()
root.geometry("215x290")
root.title("Verificação de Idade")
Application(root)
root.mainloop()