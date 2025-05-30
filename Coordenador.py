from __future__ import annotations
from Professor import Professor
from Salario import *
class Coordenador(Professor):
    def __init__(self, sistema, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel, formacao, disciplina,area,plusSalario):
        Professor.__init__(self, sistema, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel,formacao,disciplina)
        self.__area = area
        self.__plusSalario = self.getSalario().getSalarioBruto() * 0.15
        sistema.cadastroCoordenadores(self)


    def getArea(self):
        return self.__area


    def getPlusSalario(self):
        return self.__plusSalario


    def exibirCoordenadorProf(self):
        Professor.Exibir()
        print(f"{' Informações Coordenador ':-^50}")
        print(f"Área: {self.getPlusSalario()}")  
        print(f"Salário adicional: {self.getPlusSalario()}")

    def calcularPlusSalario(self):
        return self.getSalario().getSalarioLiquido() + self.getPlusSalario()