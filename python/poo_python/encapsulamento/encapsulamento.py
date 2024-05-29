class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id , nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def listaclientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self):
        del self.dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Janara')
bd.inserir_cliente(2, 'Joao')
bd.inserir_cliente(3, 'Mateus')
print(bd.dados)
#encapsulamento em outras linguagems de programacao usam o public, private, protected.  No python se criarmos na classe um atributo com o valor self.dados igual no exemplo acima ela e considerada publica, se usarmos o _ por exemplo self._dados ela e privada mas nao totalmente segura, ela ainda pode ser acessada. Para nao ser acessa sao __ exemplo self.__dados
        