class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'olá'


if __name__ == '__main__':
    pessoa = Pessoa('gustavo', 16)
    print(pessoa.nome)
    print(pessoa.idade)
    print(pessoa.cumprimentar())
