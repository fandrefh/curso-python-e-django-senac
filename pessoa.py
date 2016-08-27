class Pessoa(object):

    def __init__(self, nome, mae, idade):
        self.nome = nome
        self.mae = mae
        self.idade = idade

    def pega_nome_pessoa(self):
        return self.nome

    def somar(self):
        return 50 + 50
