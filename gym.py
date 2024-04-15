from tkinter.ttk import *
from tkinter import *

def bt_click():
      en.get()
      if (en)['text'] == 'Segunda':
         lb_resp['text'] = "Peito e Triceps" 
        
   

janela = Tk()
janela.geometry("400x400")
janela.resizable(width=FALSE, height=FALSE)


janela.title("Rotina Acadêmia")
lb = Label(janela, text="Veja qual o treino do dia!", font=("Arial 13 bold"))
lb.place(x=100, y=30)

en = Entry(janela)
en.place(x=90, y=100)

bt = Button(janela, text=('Ver treino'), command=bt_click)
bt.place(x=100, y=150)

lb_resp = Label(janela, text="Resposta")
lb_resp.place(x=100 ,y=190)


janela.mainloop()