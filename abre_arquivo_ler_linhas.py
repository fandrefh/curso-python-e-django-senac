entrada = open("mensagem.txt")
saida = open("cripto.txt", "w")
for linha in entrada.readlines():
    for letra in linha:
        if letra in "aeiou":
            saida.write("*")
        else:
            saida.write(letra)
entrada.close()
saida.close()
