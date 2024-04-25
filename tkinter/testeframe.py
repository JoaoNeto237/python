from tkinter import *

janela = Tk()
janela.title("Frame")
janela.geometry('400x400')
janela.resizable(width=FALSE, height=FALSE)

frame = Frame(janela, width=400, height=40, bg='white')
frame.grid(row=0, column=0 ,columnspan=3, padx=0, pady=2)

frame_esquerda = Frame(janela, width=100, height=260, bg='grey')
frame_esquerda.grid(row=1, column=0,padx=2, pady=2)

frame_meio = Frame(janela, width=200, height=260, bg='white')
frame_meio.grid(row=1, column=1 ,padx=2, pady=2)

frame_direita = Frame(janela, width=100, height=260, bg='grey')
frame_direita.grid(row=1, column=2 ,padx=2, pady=2)



janela.mainloop()