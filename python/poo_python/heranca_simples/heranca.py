#Super classe. Nao herda nada e a classe principal. Classe que cria configuracoes e metodos genericos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print('Falando')

# Os metodos que tiverem dentro da classe principal, vale para todos as classes que herdam  a classe principal . Por exemplo o metodo (falar). Tanto a classe (Cliente) quanto (Aluno) falam. 



#Subclasses sao as classes que herdam, classes filhas.Sao as classe que especificam, criar especificacoes para certa classe, faz como se fosse uma melhoria alem das configuracoes gerais
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} esta estudando...')



#As classe tambem podem ter seus proprios metodos que so valem para eles mesmos. Ex:
# O metodo (estudar), e um metodo exclusivo da classe (Aluno),  do mesmo jeito o metodo (comprar) e exclusivo da classe (Cliente).