import pickle


class Cuser:
    def __init__(self):
        self.nome = None
        self.dataNasc = None
        self.numBi = None
        self.tel = None
        self.email = None
        self.profi = None
        self.morada = None
        self.password = None
        self.localidade = None
        self.listDadosUser = list()
        self.listPropriedades = list()

    def lerListaPropriedades(self):
        try:
            arqP = open(f"users/{self.nome}.pkl", "rb")
            self.listPropriedades = pickle.load(arqP)
            arqP.close()
            return True
        except:
            return False

    def lerListaUser(self):
        try:
            arq = open("users/listUser.pkl", "rb")
            self.listDadosUser = pickle.load(arq)
            arq.close()
            return True
        except:
            return False

    def salvarConta(self):
        self.lerListaUser()
        dadosUser = dict()

        dadosUser["Nome"] = self.nome
        dadosUser["Data de Nascimento"] = self.dataNasc
        dadosUser["Nº do B.I"] = self.numBi
        dadosUser["Telefone"] = self.tel
        dadosUser["email"] = self.email
        dadosUser["Profissao"] = self.profi
        dadosUser["Morada"] = self.morada
        dadosUser["Palavra-passe"] = self.password

        self.listDadosUser.append(dadosUser.copy())

        arq = open("users/listUser.pkl", "wb")
        pickle.dump(self.listDadosUser, arq)
        arq.close()

        arqP = open(f"users/{self.nome}.pkl", "wb")
        pickle.dump(self.listPropriedades, arqP)
        arqP.close()

    def atualizarListpropriedades(self, name):
        arq0 = open(f"users/{name}.pkl", "wb")
        pickle.dump(self.listPropriedades, arq0)
        arq0.close()


class Cpropriety:
    def __init__(self):
        self.soli = dict()

        self.totalPropriedades = list()
        self.listSolicitar = list()

    def lerTotalPopriedades(self):
        try:
            arq = open("propriedades/totalPropriedades.pkl", "rb")
            self.totalPropriedades = pickle.load(arq)
            arq.close()
            return True
        except:
            return False

    def lerSolicitacoes(self):
        try:
            arqL = open("agencia/solicitar.pkl", "rb")
            self.listSolicitar = pickle.load(arqL)
            arqL.close()
            return True
        except:
            return False

    def activarListSolicitacoes(self):
        arqE = open("agencia/solicitar.pkl", "wb")
        pickle.dump(self.listSolicitar, arqE)
        arqE.close()

    def solicitar(self):
        arqE = open("agencia/solicitar.pkl", "wb")
        self.listSolicitar.append(self.soli.copy())
        pickle.dump(self.listSolicitar, arqE)
        arqE.close()

    def atualizarListTotalPropriedades(self):
        arq0 = open("propriedades/totalPropriedades.pkl", "wb")
        pickle.dump(self.totalPropriedades, arq0)
        arq0.close()

    def atualizarSolicitacoes(self):
        arq = open("agencia/solicitar.pkl", "wb")
        pickle.dump(self.listSolicitar, arq)
        arq.close()


class Cagent:
    def __init__(self):
        self.listAgent = list()

        self.nome = None
        self.numBi = None
        self.tel = None
        self.localidade = None
        self.password = None

    def lerListAgentes(self):
        try:
            arq = open("agencia/listFunc.pkl", "rb")
            self.listAgent = pickle.load(arq)
            arq.close()
            return True
        except:
            return False

    def salvarConta(self):
        self.lerListAgentes()
        dadosFunc = dict()

        dadosFunc["Nome"] = self.nome
        dadosFunc["Nº do B.I"] = self.numBi
        dadosFunc["Telefone"] = self.tel
        dadosFunc["Localidade"] = self.localidade
        dadosFunc["Palavra-passe"] = self.password

        self.listAgent.append(dadosFunc.copy())

        arq = open("agencia/listFunc.pkl", "wb")
        pickle.dump(self.listAgent, arq)
        arq.close()
