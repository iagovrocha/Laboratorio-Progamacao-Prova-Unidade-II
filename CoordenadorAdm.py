from __future__ import annotations
from Funcionario import Funcionario
class CoordenadorAdm(Funcionario):
    def __init__(self, sistema: Sistema, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, # type: ignore
                  diaNasc: int, sexo: str, matricula: int, setor: str, cargo: str, nivel: str, area: str):
        super().__init__(sistema, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel)
        self.__area = area
        self.__plusSalario = self.getSalario().getSalarioBruto() * 0.135


    def getArea(self):
        return self.__area

    def getPlusSalario(self):
        return self.__plusSalario

    def setArea(self, area):
        self.__area = area
    
    def setNivel(self, nivel: str):
        Funcionario.setNivel(self, nivel)
        self.__plusSalario = self.getSalario().getSalarioBruto() * 0.135

    def calcularPlusSalario(self):
        return self.getSalario().getSalarioLiquido() + self.getPlusSalario()
    
    def Exibir(self):
        Funcionario.Exibir(self)
        print(f"{' Informações Coordenador ':-^50}")
        print(f"""
            Area: {self.getArea()}
            Bonificação: R${self.getPlusSalario():.2f}
            """)