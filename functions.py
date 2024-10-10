from classes import *
from datetime import datetime
import os

usuario = Cuser()
propriedade = Cpropriety()


def tela(sect):
    print("*******************************************************************************************")
    print("                                Imobiliária Matano Nankisi")
    print("*******************************************************************************************\n\n")
    print(f"================== {sect} ==================")


def salvarConta():
    usuario.salvarConta()
    print("\033[0;32mConta salva com sucesso!!!\033[m")


def pesqPropriedades(nome):
    os.system("cls") or None

    prop = propriedade.lerTotalPopriedades()

    if not prop:
        print("\033[0;33mAinda não existem propriedades.\033[m")
        perfilUser(nome)
        return

    tela("Pesquisar Propriedade")

    op = input("Digite o I.D. da Propriedade: ")

    existe = False

    for i in range(0, len(propriedade.totalPropriedades)):
        if (str(propriedade.totalPropriedades[i]["Id"])).upper() == op.upper():
            existe = True
            break

    if not existe:
        print("\033[0;33mNão existe nenhuma propriedade com esse I.D.!!!\033[m")
        perfilUser(nome)
    else:
        apVT = "ApV"

        for j in range(0, len(propriedade.totalPropriedades)):
            if (str(propriedade.totalPropriedades[j]["Id"])).upper() == op.upper():
                apVT = propriedade.totalPropriedades[j]["APV-T"]
                break

        if apVT == "ApV":
            for k in range(0, len(propriedade.totalPropriedades)):
                if (str(propriedade.totalPropriedades[k]["Id"])).upper() == op.upper():
                    print("I.D: {}\n".format(propriedade.totalPropriedades[k]["Id"]))
                    print("Ano de Construção: {}\n".format(propriedade.totalPropriedades[k]["AnoC"]))
                    print("Área (mm2): {}\n".format(propriedade.totalPropriedades[k]["Area"]))
                    print("Localização: {}\n".format(propriedade.totalPropriedades[k]["Local"]))
                    print("Tipológia: {}\n".format(propriedade.totalPropriedades[k]["Tipo"]))
                    print("Preço (Kz): {}\n".format(propriedade.totalPropriedades[k]["Price"]))
                    print("Nome do Proprietário: {}".format(propriedade.totalPropriedades[k]["NomeP"]))

                    print("\n***** Apartamento/Vivenda *****\n")

                    print("*******************************************************************************************")
                    break
        else:
            for k in range(0, len(propriedade.totalPropriedades)):
                if (str(propriedade.totalPropriedades[k]["Id"])).upper() == op.upper():
                    print("I.D: {}\n".format(propriedade.totalPropriedades[k]["Id"]))
                    print("Área (mm2): {}\n".format(propriedade.totalPropriedades[k]["Area"]))
                    print("Localização: {}\n".format(propriedade.totalPropriedades[k]["Local"]))
                    print("Zona: {}\n".format(propriedade.totalPropriedades[k]["Zona"]))
                    print("Preço (Kz): {}\n".format(propriedade.totalPropriedades[k]["Price"]))
                    print("Nome do Proprietário: {}".format(propriedade.totalPropriedades[k]["NomeP"]))

                    print("\n***** Terreno *****\n")

                    print("*******************************************************************************************")
                    break

        perfilUser(nome)


def listarSuasPropriedades(nome):
    os.system("cls") or None

    usuario.lerListaPropriedades()

    if len(usuario.listPropriedades) == 0:
        print("\033[0;33mNenhuma propriedade registada.\033[m")
        perfilUser(nome)
        return
    else:
        tela("Lista das Suas Propriedades")

        for k in range(0, len(usuario.listPropriedades)):
            if usuario.listPropriedades[k]["APV-T"] == "ApV":
                print("I.D: {}\n".format(usuario.listPropriedades[k]["Id"]))
                print("Ano de Construção: {}\n".format(usuario.listPropriedades[k]["AnoC"]))
                print("Área (mm2): {}\n".format(usuario.listPropriedades[k]["Area"]))
                print("Localização: {}\n".format(usuario.listPropriedades[k]["Local"]))
                print("Tipológia: {}\n".format(usuario.listPropriedades[k]["Tipo"]))
                print("Preço (Kz): {}\n".format(usuario.listPropriedades[k]["Price"]))
                print("Nome do Proprietário: {}\n".format(usuario.listPropriedades[k]["NomeP"]))

                try:
                    if usuario.listPropriedades[k]["Estado"] == "Alugado":
                        print("!!!!!  Alugado até {}   !!!!!".format(usuario.listPropriedades[k]["AnoT"]))
                except:
                    print()

                print("\n***** Apartamento/Vivenda *****\n")

                print("*******************************************************************************************")

            else:
                print("I.D: {}\n".format(usuario.listPropriedades[k]["Id"]))
                print("Área (mm2): {}\n".format(usuario.listPropriedades[k]["Area"]))
                print("Localização: {}\n".format(usuario.listPropriedades[k]["Local"]))
                print("Zona: {}\n".format(usuario.listPropriedades[k]["Zona"]))
                print("Preço (Kz): {}\n".format(usuario.listPropriedades[k]["Price"]))
                print("Nome do Proprietário: {}\n".format(usuario.listPropriedades[k]["NomeP"]))

                try:
                    if usuario.listPropriedades[k]["Estado"] == "Alugado":
                        print("!!!!!  Alugado até {}   !!!!!".format(usuario.listPropriedades[k]["AnoT"]))
                except:
                    print()

                print("\n***** Terreno *****\n")

                print("*******************************************************************************************")

    perfilUser(nome)
    return


def adicionarPropriedades(nome):
    os.system("cls") or None

    prop = propriedade.lerTotalPopriedades()

    if not prop:
        print("\033[0;33mAinda não existem propriedades.\033[m")
        perfilUser(nome)
        return

    tela("solicitar Propriedades")

    for k in range(0, len(propriedade.totalPropriedades)):
        if propriedade.totalPropriedades[k]["NomeP"] != nome:
            if propriedade.totalPropriedades[k]["APV-T"] == "ApV":
                print("I.D: {}\n".format(propriedade.totalPropriedades[k]["Id"]))
                print("Ano de Construção: {}\n".format(propriedade.totalPropriedades[k]["AnoC"]))
                print("Área (mm2): {}\n".format(propriedade.totalPropriedades[k]["Area"]))
                print("Localização: {}\n".format(propriedade.totalPropriedades[k]["Local"]))
                print("Tipológia: {}\n".format(propriedade.totalPropriedades[k]["Tipo"]))
                print("Preço (Kz): {}\n".format(propriedade.totalPropriedades[k]["Price"]))
                print("Nome do Proprietário: {}".format(propriedade.totalPropriedades[k]["NomeP"]))

                print("\n***** Apartamento/Vivenda *****\n")

                print("*******************************************************************************************")

            else:
                print("I.D: {}\n".format(propriedade.totalPropriedades[k]["Id"]))
                print("Área (mm2): {}\n".format(propriedade.totalPropriedades[k]["Area"]))
                print("Localização: {}\n".format(propriedade.totalPropriedades[k]["Local"]))
                print("Zona: {}\n".format(propriedade.totalPropriedades[k]["Zona"]))
                print("Preço (Kz): {}\n".format(propriedade.totalPropriedades[k]["Price"]))
                print("Nome do Proprietário: {}".format(propriedade.totalPropriedades[k]["NomeP"]))

                print("\n***** Terreno *****\n")

                print("*******************************************************************************************")

    existe = False

    localidade = "Luanda"

    while True:
        Id = input("Digite o I.D: da Propriedade: ")

        for l in range(0, len(propriedade.totalPropriedades)):
            if propriedade.totalPropriedades[l]["NomeP"] != nome:
                if propriedade.totalPropriedades[l]["Id"] == Id:
                    localidade = propriedade.totalPropriedades[l]["Local"]
                    existe = True

        if existe:
            break
        else:
            print("\033[0;31mI.D. Inexistente!!!\033[m")
            perfilUser(nome)
            return

    print("*** Pretende: ")
    print("1 - Comprar")
    print("2 - Alugar")
    print("0 - Sair")
    op = int(input("Opção: "))
    os.system("cls") or None

    if op == 1:
        print("Comprar")
    elif op == 2:
        print("Alugar")
    elif op == 0:
        perfilUser(nome)
        return
    else:
        print("\033[0;31mOpção invalida!!!\033[m")
        perfilUser(nome)
        return

    control = propriedade.lerSolicitacoes()

    if control:
        for m in propriedade.listSolicitar:
            if m["Id"] == Id:
                print("\033[0;33mEsse Imóvel já foi solicitado!\033[m")
                perfilUser(nome)
                return
    else:
        propriedade.activarListSolicitacoes()

    propriedade.soli["NomeSolicitador"] = nome
    propriedade.soli["Id"] = Id
    propriedade.soli["Op"] = op
    propriedade.soli["Localidade"] = localidade

    propriedade.solicitar()

    print("""\033[0;32mA solicitação foi feita com sucesso!!!\033[0;33m
            Dirija-se para a agência da Imobiliária Matano Nankisi 
            mais perto de si Para fazer a possível transação\033[m
         """)

    perfilUser(nome)

    return


def removerPropriedades(nome):
    os.system("cls") or None

    prop = propriedade.lerTotalPopriedades()

    if not prop:
        print("\033[0;33mAinda não existem propriedades.\033[m")
        perfilUser(nome)
        return

    usuario.lerListaPropriedades()

    if len(usuario.listPropriedades) == 0:
        print("\033[0;33mNenhuma propriedade registada.\033[m")
        perfilUser(nome)
        return
    else:
        tela("Remover Propriedades")

    Id = input("Digite o I.D. da Propriedade que quer Remover: ")

    existeSeu = False

    for tPS in usuario.listPropriedades:
        if tPS["NomeP"] == nome and tPS["Id"] == Id:
            usuario.listPropriedades.remove(tPS)
            existeSeu = True
            break

    if not existeSeu:
        print("\033[0;31mA propriedade não é sua!!!\033[m")
        perfilUser(nome)
        return

    usuario.atualizarListpropriedades(nome)

    for tP in propriedade.totalPropriedades:
        if tP["NomeP"] == nome and tP["Id"] == Id:
            propriedade.totalPropriedades.remove(tP)

    propriedade.atualizarListTotalPropriedades()

    print("\033[0;32mPropriedade Removida com Sucesso!!!\033[m")
    perfilUser(nome)
    return


def removerAluguel(nome):
    os.system("cls") or None

    usuario.lerListaPropriedades()

    if len(usuario.listPropriedades) == 0:
        print("\033[0;33mNenhuma propriedade registada.\033[m")
        perfilUser(nome)
        return
    else:
        tela("Remover Propriedade Alugada")

    Id = input("Digite o I.D. da Propriedade que quer Remover: ")

    existeSeu = False

    for tPS in usuario.listPropriedades:
        if tPS["Id"] == Id and tPS["Estado"] == "Alugado":
            usuario.listPropriedades.remove(tPS)
            existeSeu = True
            break

    if not existeSeu:
        print("\033[0;31mA propriedade não está alugada por si.!!!\033[m")
        perfilUser(nome)
        return

    usuario.atualizarListpropriedades(nome)

    print("\033[0;32mPropriedade Removida com Sucesso!!!\033[m")
    perfilUser(nome)
    return


def perfilUser(nome):
    usuario.lerListaPropriedades()

    tela(nome + f"     Nº de Propriedades: {len(usuario.listPropriedades)}")
    print("\n================== Escolha um Opção ==================")
    print("1 - Pesquisar Propriedades")
    print("2 - Listar Suas Propriedades")
    print("3 - Solicitar Propriedade")
    print("4 - Remover Propriedade")
    print("5 - Remover Propriedade Alugada")
    print("0 - Sair")
    op = int(input("Opção: "))
    os.system("cls") or None

    if op == 1:
        pesqPropriedades(nome)
    elif op == 2:
        listarSuasPropriedades(nome)
    elif op == 3:
        adicionarPropriedades(nome)
    elif op == 4:
        removerPropriedades(nome)
    elif op == 5:
        removerAluguel(nome)
    elif op == 0:
        return
    else:
        print("\033[0;31mOpção invalida!!!\033[m")


def login():
    os.system("cls") or None

    user = usuario.lerListaUser()

    if not user:
        print("\033[0;33mAinda não existem usuários.\033[m")
        return

    acesso = False

    while True:
        tela("login")

        usuario.nome = input("Digite o Nome: ")
        usuario.password = input("Digite a Palavra-passe: ")

        for i in range(0, len(usuario.listDadosUser)):
            if usuario.listDadosUser[i]["Nome"] == usuario.nome and usuario.listDadosUser[i]["Palavra-passe"] == usuario.password:
                acesso = True

        if acesso:
            os.system("cls") or None
            perfilUser(usuario.nome)
        else:
            print(f"\033[0;31m!!!!!!!!!!!!!!!!! Senha Incorreta !!!!!!!!!!!!!!!!!\033[m")


def criarConta():
    while True:
        os.system("cls") or None
        tela("Criar Conta")

        usuario.nome = input("Nome: ")

        print("===== Data de Nascimento =====")
        dia = input("Dia: ")
        mes = input("Mês: ")
        ano = input("Ano: ")
        usuario.dataNasc = dia + "-" + mes + "-" + ano

        if (datetime.now().year - int(ano)) < 18:
            print("\033[0;33mLamntamos, mas infelizmente não tem idade suficinte para ter uma conta no nosso sistema.\033[m")
            return

        usuario.numBi = input("Nº B.I.: ")
        usuario.tel = input("Telefone: ")
        usuario.email = input("Email: ")
        usuario.profi = input("Profissão: ")
        usuario.morada = input("Morada: ")

        usuario.password = input("Palavra-passe: ")

        while usuario.password != input("Digite a Palavra-passe novamente: "):
            print("\033[0;31mPalavra-passe incorreta!!!\033[m")
            usuario.password = input("Palavra-passe: ")

        dec = (input("Deseja salvar esses dados? [S/N]: ")).upper()

        while dec not in "SN":
            print("\033[0;31mComando Invalido!!!\033[m")
            dec = (input("Deseja salvar esses dados? [S/N]: ")).upper()

        if dec == "S":
            salvarConta()
            return
        else:
            continue
