import random

qtd = int(input("Quantos nomes serao armazenados? "))

controle = 1
nomes = []

while controle <= qtd:
	nome = input("Informe o {}º nome: ".format(controle))
	nomes.append(nome)
	controle += 1

random.shuffle(nomes)
escolhido = random.choice(nomes)
print("Nome sorteado:", escolhido)