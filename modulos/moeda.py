def dobro(preco=0, formato=False):
    res = (preco * 2)
    return res if not format else moeda( res)

def metade(preco=0, formato=False):
    res = (preco / 2)
    return res if not format else moeda(res)


def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if format == False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if format == False else moeda(res)


def moeda(preco=0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',') 


def resumo(preco=0, taxaa=0, taxar=0):
    print('-'*30)
    print('RESUMO DO VALOR!'.center(30))
    print('-'*30)
    print(f'Preco analisado: {moeda(preco)}')
    print(f'O dobro do valor e: {dobro(preco)}')
    print(f'A metade do valor e: {metade(preco)}')
    print(f'Diminuindo o valor em 10%, {diminuir(preco, 10)}')
    print(f'Aumentando o valor em 20%, {aumentar(preco, 20)}')


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31m ERRO: {entrada} e um preco invalido \033[m')
        else:
            valido = True
            return float(entrada)