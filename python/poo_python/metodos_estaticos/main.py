#Metodos Estaticos 
"""

Métodos estáticos em Python são métodos definidos dentro de uma classe, mas que não operam em instâncias da classe. Eles são marcados com o decorador @staticmethod e não recebem uma referência implícita para a instância (geralmente chamada de self), como os métodos de instância normais. Em vez disso, eles se comportam mais como funções regulares, mas são logicamente organizados dentro da classe porque estão relacionados ao conceito encapsulado pela classe.

A principal diferença entre métodos estáticos e métodos de instância é que métodos de instância operam em instâncias da classe e, portanto, têm acesso aos atributos da instância usando o parâmetro self, enquanto métodos estáticos não têm acesso a qualquer instância específica e, portanto, não precisam de acesso a self. Isso os torna úteis para operações que não dependem de nenhum estado interno específico da instância.


"""
#Nao preciso de um objeto para usar um metodo estatico. Serve como um especificador
class MinhaClasse:
    def __init__(self, estado: bool) -> None:
        self.estado = estado

    @staticmethod
    
    def metodo_estatico():
        print('Estou no meu metodo estatico: D')

obj1 = MinhaClasse(True)
obj1.metodo_estatico()