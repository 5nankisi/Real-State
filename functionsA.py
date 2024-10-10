from classes import *
from functions import tela
import os
from datetime import datetime


agente = Cagent()
propriedade = Cpropriety()
usuario = Cuser()


def atender(Id, nomeVendedor, nomeDoSolicitador, interesse):
    os.system("cls") or None

    tela("Atender uma Solicitação")

    print("********************************************************************************************************************************")

    anoCX = ""
    areaX = ""
    localX = ""
    tipoX = ""
    priceX = ""
    nomePX = ""
    apVTX = ""
    zonaX = ""

    propriedade.lerTotalPopriedades()

    for i in propriedade.totalPropriedades:
        if i["Id"] == Id:
            areaX = i["Area"]
            localX = i["Local"]
            priceX = i["Price"]
            nomePX = i["NomeP"]

            if i["APV-T"] == "ApV":
                print("**************************** Apartamento/Vivenda **********************************************")
                print("""
                        I.D: {}                  Ano De Construção: {}           Área (mm2): {}
                        
                        Localização: {}          Tipológia: {}                   Preço (Kz): {}
                        
                        Nome do Proprietário: {}
                        
                        """.format(i["Id"], i["AnoC"], i["Area"], i["Local"], i["Tipo"], i["Price"], i["NomeP"]))

                anoCX = i["AnoC"]
                tipoX = i["Tipo"]
                apVTX = i["APV-T"]
                break
            else:
                print("**************************** Terreno **********************************************************")
                print("""
                        I.D: {}                  Área (mm2): {}           Localização: {}

                        Zona: {}                 Preço (Kz): {}

                        Nome do Proprietário: {}

                        """.format(i["Id"], i["Area"], i["Local"], i["Zona"], i["Price"], i["NomeP"]))

                zonaX = i["Zona"]
                apVTX = i["APV-T"]
                break

    print(f"""
            Nome do Solicitador: {nomeDoSolicitador}            Nome Do Agente: {nomeVendedor}          
                                        Data: {datetime.now()}""")

    print("********************************************************************************************************************************")

    if interesse == 1:
        print("+++ Clique: ")
        print("1 - Confirmar Compra")
        print("2 - Cancelar Compra")

        op = int(input("Opção: "))

        if op == 1:
            usuario.nome = nomePX

            usuario.lerListaPropriedades()

            for j in usuario.listPropriedades:
                if j["Id"] == Id:
                    usuario.listPropriedades.remove(j)
                    break

            usuario.atualizarListpropriedades(nomePX)

            for edit in propriedade.totalPropriedades:
                if edit["Id"] == Id:
                    edit["NomeP"] = nomeDoSolicitador
                    break

            propriedade.atualizarListTotalPropriedades()

            propriedade.lerSolicitacoes()

            for k in propriedade.listSolicitar:
                if k["Id"] == Id:
                    propriedade.listSolicitar.remove(k)
                    break

            propriedade.atualizarSolicitacoes()

            usuario.listPropriedades.clear()

            usuario.nome = nomeDoSolicitador

            usuario.lerListaPropriedades()

            add = dict()
            add["Id"] = Id
            add["Area"] = areaX
            add["Local"] = localX
            add["Price"] = priceX
            add["NomeP"] = nomeDoSolicitador

            if apVTX == "ApV":
                add["AnoC"] = anoCX
                add["Tipo"] = tipoX
                add["APV-T"] = "ApV"

                usuario.listPropriedades.append(add.copy())

                usuario.atualizarListpropriedades(nomePX)

                print("\033[0;32mCompra feita com sucesso!!!\033[m")

                arq3 = open(f"agencia/relatorio/{Id + nomeDoSolicitador + nomePX + nomeVendedor}.txt", "w")
                relatorio = f"""
                            ****************************** Compra de Apartamento/Vivenda ****************************************************
                            I.D: {Id}                  Ano De Construção: {anoCX}           Área (mm2): {areaX}
                        
                            Localização: {localX}      Tipológia: {tipoX}                   Preço (Kz): {priceX}
                            
                            Nome do Propretário: {nomePX}                                   Nome do Comprador: {nomeDoSolicitador}
                            
                            -----------------------------------------------------------------------------------------------------------------
                            Nome do Agente: {nomeVendedor}                                  Data: {datetime.now()}
                                                                
                                                              Agência: Imb. MN - {localX}
                            """
                arq3.write(relatorio)
                arq3.close()

                perfilFunc(nomeVendedor)

                return
            else:
                add["Zona"] = zonaX
                add["APV-T"] = "T"

                usuario.listPropriedades.append(add.copy())

                usuario.nome = nomeDoSolicitador

                usuario.atualizarListpropriedades(nomeDoSolicitador)

                print("\033[0;32mCompra feita com sucesso!!!\033[m")

                arq3 = open(f"agencia/relatorio/{Id + nomeDoSolicitador + nomePX + nomeVendedor}.txt", "w")

                relatorio = f"""
                            ****************************** Compra de Terreno ****************************************************************
                            I.D: {Id}                  Área (mm2): {areaX}                         Localização: {localX}  
                                
                            Zona: {zonaX}              Preço (Kz): {priceX}

                            Nome do Propretário: {nomePX}                                          Nome do Comprador: {nomeDoSolicitador}
                            
                            _________________________________________________________________________________________________________________
                            Nome do Agente: {nomeVendedor}                                         Data: {datetime.now()}
                            
                                                                Agência: Imb. MN - {localX}
                            """

                arq3.write(relatorio)
                arq3.close()

                perfilFunc(nomeVendedor)
                return
        elif op == 2:
            print("\033[0;33mCompra Cancelada!\033[m")
            perfilFunc(nomeVendedor)
            return
        else:
            print("\033[0;31mOpção Invalida!\033[m")
            perfilFunc(nomeVendedor)
            return
    else:
        print("+++ Clique: ")
        print("1 - Confirmar Aluguel")
        print("2 - Cancelar Aluguel")

        op = int(input("Opção: "))

        if op == 1:
            print("===== Data de Termino do Aluguel =====")
            dia = input("Dia: ")
            mes = input("Mês: ")
            ano = input("Ano: ")

            if datetime.now().year > int(ano):
                print("\033[0;31mO ano de término não pode ser inferior ao ano actual!!!\033[m")
                perfilFunc(nomeVendedor)
                return

            anoTermino = f"{dia}/{mes}/{ano}"

            usuario.nome = nomeDoSolicitador

            usuario.lerListaPropriedades()

            add = dict()
            add["Id"] = Id
            add["Area"] = areaX
            add["Local"] = localX
            add["Price"] = priceX
            add["NomeP"] = nomePX
            add["Estado"] = "Alugado"
            add["AnoT"] = anoTermino

            if apVTX == "ApV":
                add["AnoC"] = anoCX
                add["Tipo"] = tipoX
                add["APV-T"] = "ApV"

                usuario.listPropriedades.append(add.copy())

                propriedade.lerSolicitacoes()

                for k in propriedade.listSolicitar:
                    if k["Id"] == Id:
                        propriedade.listSolicitar.remove(k)
                        break

                propriedade.atualizarSolicitacoes()

                usuario.atualizarListpropriedades(nomeDoSolicitador)

                print("\033[0;32mCompra feito com sucesso!!!\033[m")

                arq3 = open(f"agencia/relatorio/{Id + nomeDoSolicitador + nomePX + nomeVendedor}.txt", "w")

                relatorio = f"""
                            ****************************** Aluguel de Apartamento/Vivenda ****************************************************
                            I.D: {Id}                  Ano De Construção: {anoCX}           Área (mm2): {areaX}

                            Localização: {localX}      Tipológia: {tipoX}                   Preço (Kz): {priceX}

                            Nome do Propretário: {nomePX}                                   Nome do Solicitador: {nomeDoSolicitador}
                            
                                                            Término do Aluguel: {anoTermino}
                            
                            ____________________________________________________________________________________________________________________
                            Nome do Agente: {nomeVendedor}                                  Data: {datetime.now()}
                            
                                                             Agência: Imb. MN - {localX}
                            """

                arq3.write(relatorio)
                arq3.close()

                perfilFunc(nomeVendedor)
                return
            else:
                add["Zona"] = zonaX
                add["APV-T"] = "T"

                usuario.listPropriedades.append(add.copy())

                propriedade.lerSolicitacoes()

                for k in propriedade.listSolicitar:
                    if k["Id"] == Id:
                        propriedade.listSolicitar.remove(k)
                        break

                propriedade.atualizarSolicitacoes()

                usuario.atualizarListpropriedades(nomeDoSolicitador)

                print("\033[0;32mAluguel feito com sucesso!!!\033[m")

                arq3 = open(f"agencia/relatorio/{Id + nomeDoSolicitador + nomePX + nomeVendedor}.txt", "w")

                relatorio = f"""
                            ****************************** Aluguel de Terreno ****************************************************************
                            I.D: {Id}                       Área (mm2): {areaX}                    Localização: {localX}  

                            Zona: {tipoX}                   Preço (Kz): {priceX}

                            Nome do Propretário: {nomePX}                                          Nome do Solicitador: {nomeDoSolicitador}
                            
                                                            Término do Aluguel: {anoTermino}
                                                            
                            __________________________________________________________________________________________________________________
                            Nome do Agente: {nomeVendedor}                                         Data: {datetime.now()}
                            
                                                                Agência: Imb. MN - {localX}
                            """

                arq3.write(relatorio)
                arq3.close()

                perfilFunc(nomeVendedor)
                return
        elif op == 2:
            print("\033[0;33mAluguel Cancelado!\033[m")
            perfilFunc(nomeVendedor)
            return
        else:
            print("\033[0;31mOpção Invalida!\033[m")
            perfilFunc(nomeVendedor)
            return


def verSolicita(nome, local):
    propriedade.lerSolicitacoes()

    if not propriedade.lerSolicitacoes() or len(propriedade.listSolicitar) == 0:
        print("\033[0;33mNão existem solicitações\033[m")
        perfilFunc(nome)
        return

    tela("Ver Solicitações")

    interesse = 0

    sL = False

    for l in propriedade.listSolicitar:
        if l["Localidade"] == local:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Nome do Solicitador: {}".format(l["NomeSolicitador"]))
            print("I.D. da Propriedade Solicitada: {}".format(l["Id"]))
            print("Localidade: {}".format(l["Localidade"]))

            interesse = l["Op"]

            if interesse == 1:
                print("Interesse: Compra da Propriedade")
            else:
                print("Interesse: Alugar a Propriedade")

            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            sL = True

    if not sL:
        print("\033[0;33mNão existem solicitações para esta localidade.\033[m")
        perfilFunc(nome)
        return

    existe = False
    nomeDoSolicitador = "353"

    while True:
        Id = input("Digite o I.D: da Propriedade: ")

        for n in range(0, len(propriedade.listSolicitar)):
            if propriedade.listSolicitar[n]["Id"] == Id:
                nomeDoSolicitador = propriedade.listSolicitar[n]["NomeSolicitador"]
                existe = True

        if existe:
            break
        else:
            print("\033[0;31mI.D. Inexistente!!!\033[m")
            perfilFunc(nome)
            return

    print("+++ Clica:")
    print("1 - Atender")
    print("2 - Cancelar")
    op = int(input("Opção: "))

    if op == 1:
        atender(Id, nome, nomeDoSolicitador, interesse)
    elif op == 2:
        for s in propriedade.listSolicitar:
            if s["Id"] == Id:
                propriedade.listSolicitar.remove(s)
                print("\033[0;33mSolicitação Cancelada!!!\033[m")

                propriedade.atualizarSolicitacoes()

                perfilFunc(nome)
                return
    else:
        print("\033[0;31mComando Invalido!!!\033[m")
        perfilFunc(nome)
        return


def addPropriedade(nome):
    os.system("cls") or None

    tela("Adicionar Propriedades")

    print("Qual tipo de propriedade pretende adicionar?")
    print("1 - Apartamento/Vivenda")
    print("2 - Terreno")

    op = int(input("Opção: "))

    add = dict()

    if op == 1:
        print("================== Adicionar Apartamento/Vivenda ==================")
        add["Id"] = input("Digite o I.D. da propriedade: ")
        add["AnoC"] = input("Digite o Ano de Construção: ")
        add["Area"] = str(float(input("Digite a Área da Propriedade (mm2): "))) + "mXm"
        add["Local"] = input("Digite a Localização da Propriedade: ")
        add["Tipo"] = input("Digite o Tipo do Apertamento/Vivenda: ")
        add["Price"] = str(float(input("Digite o Preço da Propriedade (Kz): "))) + "Kz"
        add["NomeP"] = input("Digite o Nome do Proprietário: ")
        add["APV-T"] = "ApV"

        dec = (input("Deseja salvar esses dados? [S/N]: ")).upper()

        while dec not in "SN":
            print("\033[0;31mComando Invalido!!!\033[m")
            dec = (input("Deseja salvar esses dados? [S/N]: ")).upper()

        if dec != "S":
            perfilFunc(nome)
            return

        usuario.nome = add["NomeP"]

        control = usuario.lerListaPropriedades()

        if not control:
            print("\033[0;31mEsse nome não existe em nosso sistema.\033[m")
            perfilFunc(nome)
            return

        usuario.listPropriedades.append(add.copy())

        usuario.atualizarListpropriedades(usuario.nome)

        propriedade.lerTotalPopriedades()

        propriedade.totalPropriedades.append(add.copy())

        propriedade.atualizarListTotalPropriedades()

        print("\033[0;32mPropriedade Adicionada com Sucesso!!!\033[m")

        arq3 = open("agencia/relatorio/{}.txt".format(add["Id"] + add["NomeP"]), "w")

        relatorio = """
                    ****************************** Adição de Apartamento/Vivenda ******************************
                    I.D: {}                  Ano De Construção: {}           Área (mm2): {}

                    Localização: {}          Tipológia: {}                   Preço (Kz): {}

                                             Nome do Propretário: {}

                    Nome do Agente: {}       Agência: Imb. MN - {}      Data: {}
                    """.format(add["Id"], add["AnoC"], add["Area"], add["Local"], add["Tipo"], add["Price"],
                               add["NomeP"], nome, add["Local"], datetime.now())

        arq3.write(relatorio)
        arq3.close()

        perfilFunc(nome)

        return
    elif op == 2:
        print("================== Adicionar Terreno ==================")
        add["Id"] = input("Digite o I.D. da propriedade: ")
        add["Area"] = str(float(input("Digite a Área da Propriedade (mm2): "))) + "mXm"
        add["Local"] = input("Digite a Localização da Propriedade: ")
        add["Zona"] = input("Digite a Zona da Propriedade: ")
        add["Price"] = str(float(input("Digite o Preço da Propriedade (Kz): "))) + "Kz"
        add["NomeP"] = input("Digite o Nome do Proprietário: ")
        add["APV-T"] = "T"

        dec = (input("Deseja salvar esses dados? [S/N]: ")).upper()

        while dec not in "SN":
            print("\033[0;31mComando Invalido!!!\033[m")
            dec = (input("Deseja salvar esses dados? [S/N]: ")).upper()

        if dec != "S":
            perfilFunc(nome)
            return

        usuario.nome = add["NomeP"]

        control = usuario.lerListaPropriedades()

        if not control:
            print("\033[0;31mEsse nome não existe em nosso sistema.\033[m")
            perfilFunc(nome)
            return

        usuario.listPropriedades.append(add.copy())

        usuario.atualizarListpropriedades(usuario.nome)

        propriedade.lerTotalPopriedades()

        propriedade.totalPropriedades.append(add.copy())

        propriedade.atualizarListTotalPropriedades()

        print("\033[0;32mPropriedade Adicionada com Sucesso!!!\033[m")

        arq3 = open("agencia/relatorio/{}.txt".format(add["Id"] + add["NomeP"]), "w")

        relatorio = """
                    ****************************** Adição de Terreno ******************************
                    I.D: {}                    Área (mm2): {}               Localização: {} 
                             
                    Zona: {}                   Preço (Kz): {}

                                               Nome do Propretário: {}

                    Nome do Agente: {}         Agência: Imb. MN - {}      Data: {}
                    """.format(add["Id"], add["Area"], add["Local"], add["Zona"], add["Price"], add["NomeP"], nome,
                               add["Local"], datetime.now())

        arq3.write(relatorio)
        arq3.close()

        perfilFunc(nome)
        return
    else:
        print("\033[0;31mOpção Invalida!!!\033[m")
        return


def perfilFunc(nome):
    agente.lerListAgentes()

    local = "Luanda"

    for i in agente.listAgent:
        if i["Nome"] == nome:
            local = i["Localidade"]
            break

    tela(f"Agente: {nome}   ---------  Agência: Imb. MN - {local}")

    print("\n================== Escolha um Opção ==================")
    print("1 - Ver Solicitações")
    print("2 - Adicionar uma Propriedade")
    print("0 - Sair")
    op = int(input("Opção: "))
    os.system("cls") or None

    if op == 1:
        verSolicita(nome, local)
    elif op == 2:
        addPropriedade(nome)
    elif op == 0:
        return
    else:
        print("\033[0;31mOpção invalida!!!\033[m")


def login():
    os.system("cls") or None

    user = agente.lerListAgentes()

    if not user:
        print("\033[0;33mAinda não existem funcioários.\033[m")
        return

    acesso = False

    while True:
        tela("login")
        agente.nome = input("Digite o Nome: ")
        agente.password = input("Digite a Palavra-passe: ")

        for i in range(0, len(agente.listAgent)):
            if agente.listAgent[i]["Nome"] == agente.nome and agente.listAgent[i]["Palavra-passe"] == agente.password:
                acesso = True

        if acesso:
            os.system("cls") or None
            perfilFunc(agente.nome)
        else:
            print(f"\033[0;31m!!!!!!!!!!!!!!!!! Senha Incorreta !!!!!!!!!!!!!!!!!\033[m")


def salvarConta():
    agente.salvarConta()
    print("\033[0;32mConta salva com sucesso!!!\033[m")


def criarConta():
    while True:
        os.system("cls") or None

        tela("Criar Conta De Agente")

        agente.nome = input("Nome: ")

        agente.numBi = input("Nº B.I.: ")
        agente.tel = input("Telefone: ")
        agente.localidade = input("Localidade: ")

        agente.password = input("Palavra-passe: ")

        while agente.password != input("Digite a Palavra-passe novamente: "):
            print("\033[0;31mPalavra-passe incorreta!!!\033[m")
            agente.password = input("Palavra-passe: ")

        dec = (input("Deseja salvar esses dados? [S/N]: ")).upper()

        while dec not in "SN":
            print("\033[0;31mComando Invalido!!!\033[m")
            dec = (input("Deseja salvar esses dados? [S/N]: ")).upper()

        if dec == "S":
            salvarConta()
            return
        else:
            continue
