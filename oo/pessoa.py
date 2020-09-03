class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    juliano = Pessoa(nome='Juliano')
    renzo = Pessoa(juliano, nome='Renzo')
    print(Pessoa.cumprimentar(renzo))
    print(id(renzo))
    print(renzo.cumprimentar())
    print(renzo.nome)
    print(renzo.idade)
    for filho in renzo.filhos:
        print(filho.nome)
    renzo.sobrenome = 'Lemos'
    renzo.olhos = 1
    del renzo.olhos
    print(renzo.sobrenome)
    del renzo.filhos
    print(juliano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(juliano.olhos)
    print(id(Pessoa.olhos), id(juliano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), juliano.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classes(), juliano.nome_e_atributo_de_classes())