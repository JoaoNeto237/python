from random import randint
# Metodos de Classes
from datetime import datetime
class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

#As funcoes que estiverem dentro de classe sao metodos de instância 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#A chamada do self é para referir a instância
#OBS: pode ser qualquer nome

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

#metodos de classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        #Váriavel de escopo local
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gera_id():
        return randint(1, 10)

#A chamada cls é para referir a classe. OBS: pode ser qualquer nome

p1 = Pessoa.por_ano_nascimento('Luiz', 2000)
print(p1.idade)
p1.get_ano_nascimento( )
print(Pessoa.gera_id())