from agregacao import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 1000)
p3 = Produto('Caneca', 15)
p4 = Produto('Fone', 50)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p4)

carrinho.lista_produto()
print('A soma total deu ',  carrinho.soma_total())

#Agregacao de uma classe na outra. Para que uma classe funciona corretamente ela precisa da outra (Ela pode existir sem a outra, mas so com agregacao ela faz tudo que pode, usando as funcionaldades da outra classe).