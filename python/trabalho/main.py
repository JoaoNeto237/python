from tkinter import *
import smtplib

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Calibri", "8")

        self.container1 = Frame(master)
        self.container1["padx"] = 5
        self.container1.place(x = 10, y = 0)

        self.container2 = Frame(master)
        self.container2["pady"] = -100
        self.container2["padx"] = 5
        self.container2.place(x = 10, y = 25)

        self.container3 = Frame(master)
        self.container3["pady"] = -100
        self.container3["padx"] = 5
        self.container3.place(x = 10, y = 50)

        self.container4 = Frame(master)
        self.container4["pady"] = 6
        self.container4["padx"] = 5
        self.container4.place(x = 10, y = 75)

        self.container5 = Frame(master)
        self.container5["pady"] = 6
        self.container5["padx"] = 5
        self.container5.place(x = 10, y = 100)

        self.container6 = Frame(master)
        self.container6["pady"] = 6
        self.container6["padx"] = 5
        self.container6.place(x = 10, y = 125)

        self.container7 = Frame(master)
        self.container7["pady"] = 6
        self.container7["padx"] = 5
        self.container7.place(x = 10, y = 150)

        self.container8 = Frame(master)
        self.container8["pady"] = 6
        self.container8["padx"] = 5
        self.container8.place(x = 10, y = 175)

        self.container9 = Frame(master)
        self.container9["pady"] = 6
        self.container9["padx"] = 5
        self.container9.place(x = 10, y = 200)

        self.container10 = Frame(master)
        self.container10["pady"] = 6
        self.container10["padx"] = 5
        self.container10.place(x = 10, y = 225)

        self.container11 = Frame(master)
        self.container11["pady"] = 6
        self.container11["padx"] = 5
        self.container11.place(x = 10, y = 250)

        self.container12 = Frame(master)
        self.container12["pady"] = 6
        self.container12["padx"] = 5
        self.container12.place(x = 10, y = 275)

        self.container13 = Frame(master)
        self.container13["pady"] = 6
        self.container13["padx"] = 5
        self.container13.place(x = 10, y = 300)

        self.container14 = Frame(master)
        self.container14["pady"] = 6
        self.container14["padx"] = 5
        self.container14.place(x = 10, y = 325)

        self.container15 = Frame(master)
        self.container15["pady"] = 6
        self.container15["padx"] = 5
        self.container15.place(x = 10, y = 355)

        self.titulo = Label(self.container1, text="Automação E-mail")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack(side=LEFT)

        self.nomeLabel = Label(self.container2, text="Nome: ")
        self.nomeLabel["font"] = self.fontePadrao
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.container3)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT) 

        self.sobrenomeLabel = Label(self.container4, text="Sobrenome: ")
        self.sobrenomeLabel["font"] = self.fontePadrao
        self.sobrenomeLabel.pack(side=LEFT)

        self.sobrenome = Entry(self.container5)
        self.sobrenome["width"] = 30
        self.sobrenome["font"] = self.fontePadrao
        self.sobrenome.pack(side=LEFT)

        self.telefoneLabel = Label(self.container6, text="Telefone: ")
        self.telefoneLabel["font"] = self.fontePadrao
        self.telefoneLabel.pack(side=LEFT)

        self.telefone = Entry(self.container7)
        self.telefone["width"] = 30
        self.telefone["font"] = self.fontePadrao
        self.telefone.pack(side=LEFT)

        self.emailLabel = Label(self.container8, text="E-mail: ")
        self.emailLabel["font"] = self.fontePadrao
        self.emailLabel.pack(side=LEFT)

        self.email = Entry(self.container9)
        self.email["width"] = 30
        self.email["font"] = self.fontePadrao
        self.email.pack(side=LEFT)

        self.senhaLabel = Label(self.container10, text="Senha: ")
        self.senhaLabel["font"] = self.fontePadrao
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.container11)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)

        self.confSenhaLabel = Label(self.container12, text="Confirme a senha: ")
        self.confSenhaLabel["font"] = self.fontePadrao
        self.confSenhaLabel.pack(side=LEFT)

        self.confSenha = Entry(self.container13)
        self.confSenha["width"] = 30
        self.confSenha["font"] = self.fontePadrao
        self.confSenha.pack(side=LEFT)

        self.enviar = Button(self.container14)
        self.enviar["text"] = "Enviar"
        self.enviar["font"] = ("Arial", "7", "bold")
        self.enviar["width"]= 30
        self.enviar["command"] = self.autenticar
        self.enviar.pack()

        self.mensagemLabel = Label(self.container15, text="", font=self.fontePadrao)
        self.mensagemLabel.pack(side=LEFT)

    def autenticar(self):
        import email.message
        nome = self.nome.get()
        sobrenome = self.sobrenome.get()
        telefone = self.telefone.get()
        emaill = self.email.get()
        senha = self.senha.get()

        corpo_email = """
        <p>  Aplicado na Interface <var>nome</var></p>
        <script
        <p>aaaa </p>
        """

        msg = email.message.Message()
        msg['Subject'] = "Automacao de e-mail em python"
        msg['From'] = "kenedy.rodriguesdealmeida@gmail.com"
        msg['To'] = emaill
        password = "mipaldptclanfeai"
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email )


        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado!')

root = Tk()
root.geometry("215x390")
root.title("Automação E-mail")
Application(root)
root.mainloop()