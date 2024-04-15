from tkinter import *

#def bt_click():
   # lb2['text'] = 
  
    

janela = Tk()

janela.title("Rotina Acadêmia")
lb = Label(janela, text="Digite o dia da semana e veja qual é o treino do dia!")
lb.place(x=100, y=30)

treino = Entry(janela, width=20)
treino.place(x=100, y=70)

bt = Button(janela, text=("Ver treino"))
bt.place(x=110, y=100)


#"segunda:Quadriceps terca: Peito e Triceps quarta:(Ombros) quinta: (Costas e Biceps) sexta: Pernas: (Posterior)"
janela.geometry("400x400")
janela.mainloop()