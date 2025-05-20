import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int,
                  diaNasc: int, sexo: str, matricula: int, setor: str, cargo: str, nivel: int):
        Pessoa.__init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo)
        self.__matricula = matricula
        self.__setor = setor
        self.__cargo = cargo
        self.__nivel = nivel