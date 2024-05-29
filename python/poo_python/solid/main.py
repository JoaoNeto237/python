#nesse codigo esta sendo aplicado somente o principio de S. Principio de responsabilidade unica!
class SistemaCadastral: 
    def cadastrar(self, nome: str, idade : int) -> None:
       if self.__verificar_dados(nome, idade):
            self.__armazenar_dados(nome, idade)
       else:
           self.__indicar_erro()
        
            
    def __verificar_dados(self, nome:str, idade:int)->None:
            if isinstance(nome, str) and isinstance(idade , int):
                return True
            else:
                return False

    def __armazenar_dados(self, nome:str, idade:int)->None:
        print('Acessando o banco de dados...')
        print(f'Cadastrar o usuario { nome}, idade {idade}')

    def __indicar_erro(self)->None:
         print('Dados invalidos')



p1 = SistemaCadastral()
p1.cadastrar('ola''ola')

"""
Principio de SOLID  
S - Princípio da Responsabilidade Única (Single Responsibility Principle):
O - Princípio do Aberto/Fechado (Open/Closed Principle):
L - Princípio da Substituição de Liskov (Liskov Substitution Principle):
I - Princípio da Segregação de Interfaces (Interface Segregation Principle):
D - Princípio da Inversão de Dependência (Dependency Inversion Principle):
"""