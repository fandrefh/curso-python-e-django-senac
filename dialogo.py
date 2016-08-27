try:
	dialogo = open("dialogoss.txt")
	dialogo.seek(0)
	for linha in dialogo:
		try:
			if not linha.find(":") == -1:
				ator, fala = linha.split(":")
				print(ator, end="")
				print(" fala:", end="")
				print(fala, end="")
		except ValueError:
			print("Erro na leitura do arquivo")
	dialogo.close()
except:
	print("Arquivo nao encontrado...")

