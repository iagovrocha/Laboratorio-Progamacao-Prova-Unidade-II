from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__anoNasc = anoNasc
        self.__mesNasc = mesNasc
        self.__diaNasc = diaNasc
        self.__sexo = sexo


    def getNome(self):
        return self.__nome
    def getRg(self):
        return self.__rg
    def getCpf(self):
        return self.__cpf
    def getAnoNasc(self):
        return self.__anoNasc
    def getMesNasc(self):
        return self.__mesNasc
    def getDiaNasc(self):
        return self.__diaNasc
    def getSexo(self):
        return self.__sexo

    def Exibir(self):
        print(f"{' Informações Pessoais ':-^50}")
        print(f"""
            Nome: {self.getNome()}
            RG: {self.getRg()}
            CPF: {self.getCpf()}
            Ano de Nascimento: {self.getAnoNasc()}
            Mês de Nascimento:{self.getMesNasc()}
            Dia de Nascimento: {self.getDiaNasc()}
            Sexo: {self.getSexo()}\n""")
    def Cadastrar(self):
        pass
            