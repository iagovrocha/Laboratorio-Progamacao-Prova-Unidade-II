
class Pessoa:
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__anoNasc = anoNasc
        self.__mesNasc = mesNasc
        self.__diaNasc = diaNasc
        self.__sexo = sexo
