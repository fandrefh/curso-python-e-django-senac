import os

print("O que você deseja fazer? \
1 - Criar diretório; 2 - Limpar a tela; 3 - Verificar diretório atual.")
option = int(input())

if option == 1:
    print("Qual o nome do diretório?")
    dir_name = input()
    os.mkdir(dir_name)
elif option == 2:
    os.system('clear')
elif option == 3:
    print('Voce esta em:', os.getcwd())
    
print('Obrigado por usar nosso programa! ;-)')
