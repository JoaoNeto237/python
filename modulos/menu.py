from time import sleep


def arqExist(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criacao do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')



def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO! Por favor, digite um numero valido.')
            continue
        else:
            return n
            

def lin(tam=42):
    return '-' * tam
    
    
def txt(msg):
    print(lin())
    print(msg.center(42))
    print(lin())
    
    
def menu(lista):
    txt('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(lin())
    opc = leiaInt('Sua opcao: ')
    return opc
    
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        txt('PESSOAS CADASTRADAS.')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:        
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.\n')
            a.close()

arq = 'cursoemvideo.txt'

if not arqExist(arq): 
    criarArq(arq)



txt( 'Sistema' )
while True:
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa' ,'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp ==2:
        txt('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resp ==3:
        txt('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO. Por favor, digite uma opção válida ')
    sleep(2)