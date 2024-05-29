from associacao import Escritor
from associacao import Caneta
from associacao import MaquinaDeEscrever

escritor = Escritor('Joao')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
print(escritor.nome)
print(caneta.marca)
maquina.escrever()
caneta.escrever()
#Ate agora o programa esta printando e fazendo apenas as chamadas das funcoes que foram criados em cada uma das classes


#Embaixo esta ocorrendo uma associacao de classe, a classe escritor esta associando a classe caneta a ela.
escritor.ferramenta = caneta

#Quando a classe escritor manda escrever. Oque vai ser escrito e oq foi escrito na funcao da classe caneta pois o comando (escritor.ferramenta = caneta) esta fazendo a associacao de classes! Quando eu associo eu estou enviando oque foi criado na classe para o atributo (ferramenta) nesse exemplo
escritor.ferramenta.escrever()