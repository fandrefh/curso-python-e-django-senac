from pessoa import Pessoa
from filho import Filho

p1 = Pessoa("Francisco Andre", "Maria", 35)

print("Dados da Pessoa:")
print("Nome:", p1.nome)
print("Mae:", p1.mae)
print("Idade:", p1.idade)
print("Chamada do metodo somar a partir da classe Pessoa()")
print(p1.somar())
print()

f1 = Filho(nome="Joao", mae="Mae do Joao", idade=10)

print("Dados do Filho:")
print("Nome:", f1.nome)
print("Mae:", f1.mae)
print("Idade:", f1.idade)
print("Chamada do metodo somar a partir da classe Filho()")
print(f1.somar(10, 10))
