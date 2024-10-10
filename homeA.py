from functionsA import *

def homeAInit():
    while True:
        tela("Escolha uma Opção")
        print("================== Agência ==================")

        print("1 - Fazer Login")
        print("2 - Criar uma Conta de Agente")
        print("0 - Sair")
        op = int(input("Opção: "))
        os.system("cls") or None

        if op == 1:
            login()
        elif op == 2:
            criarConta()
        elif op == 0:
            break
        else:
            print("\033[0;31mOpção invalida!!!\033[m")
