arquivo = open("numeros.txt", "w")

for n in range(0,101):
    if n % 2 == 0:
        arquivo.write('{}\n'.format(n))
arquivo.close()
