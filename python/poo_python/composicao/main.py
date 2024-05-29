from composicao import Cliente, Endereco

cliente1 = Cliente('Joao', 20)
cliente1.inserir_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()


cliente2 = Cliente('Maria', 30)
cliente2.inserir_endereco('Salvador', 'BA')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Ana Clara', 34)
cliente3.inserir_endereco('Rio de Janeiro', 'RJ')
print(cliente3.nome)
cliente3.lista_enderecos()
print('############################### ')