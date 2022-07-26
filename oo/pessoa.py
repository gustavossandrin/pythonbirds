class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'olá'


if __name__ == '__main__':
    jasiel = Pessoa(nome='jasiel', idade=2)
    gustavo = Pessoa(jasiel, nome='gustavo', idade=16)
    print(gustavo.nome)
    print(gustavo.idade)
    print(gustavo.cumprimentar())
    gustavo.sobrenome = 'sandrin'
    del jasiel.filhos
    for filho in gustavo.filhos:
        print(filho.nome)
    print(gustavo.__dict__)
    print(jasiel.__dict__)
