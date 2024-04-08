from tkinter import *

janela = Tk()

login = Label(janela, text='Login: ')
login.grid(row=1, column=1)
en = Entry(janela)
en.grid(row=1, column=2)
senha = Label(janela , text='Senha: ')
senha.grid(row=2, column=1)
en2 = Entry(janela)
en2.grid(row=2, column=2)
bt = Button(janela, text='Confirmar')
bt.grid(row=3, column=2)


janela.geometry('300x300')
janela.mainloop()