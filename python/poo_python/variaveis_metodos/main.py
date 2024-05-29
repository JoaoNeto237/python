"""class MinhaClasse:
    
    estatico = 'Goku' #Variavel de Classe ou Variaveis Estaticas. Nao e recomendavel o uso de variaveis estaticas pelo fato de: isso pode ser abstraido pelo proprio contesto da classe no  metodo em si . Nao e uma boa pratica

    def __init__(self, estado)->None:
        self.estado = estado

    def print_estatico(self):
        print(self.estatico)


#Metodos de Classe

    @classmethod

    #cls aqui e como se eu estive pegando a propria classe em si e atribuindo o valor para ela.

    def mudar_estatico(cls):
        cls.estatico = 'Programador'
        

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.mudar_estatico()

obj1.print_estatico()
obj2.print_estatico()


"""


class Loja:

    tarifa = 1.03

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def apresentar_endereco(self)->None:
        print(self.__endereco)

    @classmethod

    def vender(cls) ->int:
        return 40 * cls.tarifa

    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) -> None:
        cls.tarifa = nova_tarifa


loja_prai = Loja('Praia')
loja_centro = Loja('Centro')   

loja_prai.apresentar_endereco()

print(loja_prai.vender())
print(loja_centro.vender())

loja_centro.alterar_tarifa(1.50)

print(loja_prai.vender())
print(loja_centro.vender())

