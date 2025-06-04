from __future__ import annotations
from Professor import Professor
from Salario import *

class Coordenador(Professor):
    def __init__(self, sistema: Sistema, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, # type: ignore
                  diaNasc: int, sexo: str, matricula: int, setor: str, cargo: str, nivel: str, formacao: str, disciplina: str, area: str):
        Professor.__init__(self, sistema, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel, formacao, disciplina)
        self.__area = area
        self.__plusSalario = self.getSalario().getSalarioBruto() * 0.15
        sistema.cadastrarCoordenadores(self)

    def getArea(self):
        return self.__area

    def getPlusSalario(self):
        return self.__plusSalario

    def setArea(self, area):
        self.__area = area
    
    def setNivel(self, nivel: str):
        Professor.setNivel(self, nivel)
        self.__plusSalario = self.getSalario().getSalarioBruto() * 0.15

    def calcularPlusSalario(self):
        return self.getSalario().getSalarioLiquido() + self.getPlusSalario()
    
    def Exibir(self):
        Professor.Exibir(self)
        print(f"{' Informações Coordenador ':-^50}")
        print(f"""
            Área: {self.getArea()}
            Bonificação: R${self.getPlusSalario():.2f}
            Salário + Bonificação: R${self.calcularPlusSalario():.2f}
            """)