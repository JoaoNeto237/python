from tkinter import *

janela = Tk()
janela.title("Frame")
janela.geometry('400x400')

#Criando o Frame(Frame pode ser usado como classe e serve como base para implementar widgets complexos. Usado para organizar um grupo de widgets!)
frame = Frame(janela, width=200, height=100, bg='blue')
frame.grid(row=0, column=0 ,padx=2, pady=2)

frame2 = Frame(janela, width=200, height=100, bg='black')
frame2.grid(row=0, column=1,padx=2, pady=2)

frame3 = Frame(janela, width=200, height=100, bg='pink')
frame3.grid(row=1, column=0 ,padx=2, pady=2)

frame4 = Frame(janela, width=200, height=100, bg='purple')
frame4.grid(row=1, column=1 ,padx=2, pady=2)

#Colocando frames dentro de frames
frame5 = Frame(frame, width=30, height=20, bg='black' )
frame5.grid(row=0, column=0)

janela.mainloop()