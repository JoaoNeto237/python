class Pessoa:#substantivo
    def __init__(self,nome: str,idade: int) -> None:#substantivo
        self.nome = nome
        self.idade = idade

    def dirigir(self, veiculo: str) -> None: #verbos
        print(f'Dirigindo um (a) {veiculo}')

    def cantar(self) -> None: #verbos
        print('Lalalala')

    def apresentar_idade(self) -> int: #verbos
        return self.idade