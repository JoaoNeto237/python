class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * ( percentual / 100))

    #Getter vai obter o que tiver aqui
    @property
    def preco(self):
        return self._preco
    
    #Setter vai setar configurar alguma coisa, nesse exemplo vai substituir R$ por nada, no caso do usuario digitar isso e der erro, como se fosse uma protecao acaso o codigo apresente algum erro usando o setter voce pode configurar isso
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor

#Nesse exemplo eu uso o setter para configurar que as letras do nome dos produtos sejam todas minusculas!

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor.lower()

p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Caneca', 20)
p2.desconto(10)
print(p2.nome, p2.preco)
