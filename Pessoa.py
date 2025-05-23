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


    def get_nome(self):
        return self.__nome

    def get_rg(self):
        return self.__rg

    def get_cpf(self):
        return self.__cpf

    def get_anoNasc(self):
        return self.__anoNasc

    def get_mesNasc(self):
        return self.__mesNasc

    def get_diaNasc(self):
        return self.__diaNasc

    def get_sexo(self):
        return self.__sexo
    def Exibir(self):
        print(f'Nome: {self.get_nome()}, rg: {self.get_rg()}, cpf: {self.get_cpf()}, ano de Nascimento: {self.get_anoNasc()}, Mês de Nascimento:{self.get_mesNasc()}, Dia de Nascimento: {self.get_diaNasc()}, Sexo: {self.get_sexo()}')
    def Cadastrar(self):
        pass
            