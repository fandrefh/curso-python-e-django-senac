from pessoa import Pessoa

class Filho(Pessoa):

    def __init__(self, **kwargs):
        super(Filho, self).__init__(**kwargs)

    def aniversario(self):
        self.idade += 1

    def caminhar(self):
        print("Aprendendo a caminhar")

    def chorar(self):
        print("Muleque chorando...")

    def pega_nome_pessoa(self):
        return "Alguma coisa diferente..."

    def somar(self, n1, n2):
        return n1 + n2
