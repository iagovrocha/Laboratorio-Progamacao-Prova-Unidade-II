from __future__ import annotations
from Pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, sistema: Sistema, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, # type: ignore
                  diaNasc: int, sexo: str, matricula: int, setor: str, cargo: str, nivel: int):
        Pessoa.__init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo)
        self.sistema = sistema
        self.__matricula = matricula
        self.__setor = setor
        self.__cargo = cargo
        self.__nivel = nivel
        self.sistema.cadastrarFuncionario(self)

    def getMatricula(self) -> str:
        return self.__matricula
    def getSetor(self) -> str:
        return self.__setor
    def getCargo(self) -> str:
        return self.__cargo
    def getNivel(self) -> int:
        return self.__nivel

    def Exibir(self):
        Pessoa.Exibir(self)
        print(f"{' Informações Funcionario ':-^50}")
        print(f"""
            Matricula: {self.getMatricula()}
            Setor: {self.getSetor()}
            Cargo: {self.getCargo()}
            Nivel: {self.getNivel()}
            """)