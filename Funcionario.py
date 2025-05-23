from __future__ import annotations
from Pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, sistema: "Sistema", nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int,
                  diaNasc: int, sexo: str, matricula: int, setor: str, cargo: str, nivel: int):
        Pessoa.__init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo)
        self.sistema = sistema
        self.__matricula = matricula
        self.__setor = setor
        self.__cargo = cargo
        self.__nivel = nivel

    def cadastrarFuncionario(self):
        self.sistema.cadastroFuncionario(self)