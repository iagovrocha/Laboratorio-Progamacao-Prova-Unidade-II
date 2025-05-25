from __future__ import annotations
from Funcionario import Funcionario
class CoordenadorAdm(Funcionario):
    def __init__(self, sistema: Sistema, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, # type: ignore
                  diaNasc: int, sexo: str, matricula: int, setor: str, cargo: str, nivel: str, area: str):
        super().__init__(sistema, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel)
        self.__area = area
        sistema.cadastrarCoordenadoresAdministrativo(self)