from __future__ import annotations

# Usando Strategy Desing Partter
class Salario:
    # def __init__(self, salarioBruto: float, salarioLiquido: float, inss: float, irrf: float, planoSaude: float, strategy: Strategy): # type: ignore
    def __init__(self, strategy: Strategy): # type: ignore
        self.__salarioBruto = 0.0
        self.__inss = 0.0
        self.__irrf = 0.0
        self.__planoSaude = 175
        self._strategy = strategy
        self.__salarioLiquido = self.calcularSalario()

    def getSalarioBruto(self) -> float:
        return self.__salarioBruto

    def getSalarioLiquido(self) -> float:
        return self.__salarioLiquido

    def getINSS(self) -> float:
        return self.__inss

    def getIRRF(self) -> float:
        return self.__irrf

    def getPlanoSaude(self) -> float:
        return self.__planoSaude
    
    # def setSalarioBruto(self, salarioBruto):
    #     self.__salarioBruto = salarioBruto
    
    # def setSalarioLiquido(self, salarioLiquido):
    #     self.__salarioLiquido = salarioLiquido

    def setINSS(self, inss):
        self.__inss = inss

    def setIRRF(self, irrf):
        self.__irrf = irrf

    def setPlanoSaude(self, planoSaude):
        self.__planoSaude = planoSaude

    def calcularSalario(self) -> float:
        if self._strategy:
            self.__salarioBruto = self._strategy.salario()
            # print(self.getSalarioBruto())
            if self.getSalarioBruto() <= 1.518:
                self.setINSS(self.getSalarioBruto() * 0.075)

            elif self.getSalarioBruto() <= 2793.88:
                self.setINSS(self.getSalarioBruto() * 0.09)

            elif self.getSalarioBruto() <= 4190.3:
                self.setINSS(self.getSalarioBruto() * 0.12)
            else:
                self.setINSS(self.getSalarioBruto() * 0.14)

            if 2259.20 < self.getSalarioBruto() <= 2826.65:
                self.setIRRF(self.getSalarioBruto() * 0.075)

            elif self.getSalarioBruto() <= 3751.05:
                self.setIRRF(self.getSalarioBruto() * 0.15)

            elif self.getSalarioBruto() <= 4664.68:
                self.setIRRF(self.getSalarioBruto() * 0.225)

            else:
                self.setIRRF(self.getSalarioBruto() * 0.275)

            self.__salarioLiquido = self.getSalarioBruto() - self.getINSS() - self.getIRRF() - self.getPlanoSaude()
            return self.getSalarioLiquido()


#Podemos incluir no menu escolhas pedindo qual o nivel do professor
    # [1] - Professor Nivel I
    # [2] - Professor Nivel II
    # [3] - Professor Nivel III

class ProfessorNivelI:
    def salario(coord):
        return 4530
class ProfessorNivelII:
    def salario(coord):
        return 5325.50
class ProfessorNivelIII:
    def salario():
        return 8568.43

    # [1] - Tecnico Administrativo Nivel A
    # [2] - Tecnico Administrativo Nivel B
    # [3] - Tecnico Administrativo Nivel C
    # [4] - Tecnico Administrativo Nivel D
    # [5] - Tecnico Administrativo Nivel E

class TecnicoAdministrativoA:
    def salario():
        return 1520.25
    
class TecnicoAdministrativoB:
    def salario():
        return 2362.67
    
class TecnicoAdministrativoC:
    def salario():
        return 2988.92
    
class TecnicoAdministrativoD:
    def salario():
        return 3572.77
    
class TecnicoAdministrativoE:
    def salario():
        return 4878.67
    


# Quais são as alíquotas do INSS em 2025?
# As alíquotas de contribuição do INSS 2025 variam de acordo com as faixas salariais. Em 2025, a tabela é:

# – Até R$1.518: 7,5%; 

# – De R$1.518,01 até R$2.793,88: 9%; 

# – De R$2.793,89 até R$4.190,83: 12%; 

# – De R$4.190,84 até R$8.157,41: 14%.


# Como fazer o cálculo do imposto?
# A conta do IR depende de uma tabela dividida em quatro faixas de renda, com uma alíquota progressiva que vai de 7,5% a 27,5%. A faixa máxima atinge os salários acima de R$ 4.664,68.

# Veja abaixo as faixas e as respectivas alíquotas em vigor ao longo de 2024:

# Faixa 1: Até R$ 2.259,20: isento
# Faixa 2: De 2.259,21 até 2.826,65: 7,5% | dedução: R$ 169,44
# Faixa 3: De 2.826,66 até 3.751,05: 15% | dedução: R$ 381,44
# Faixa 4: De 3.751,07 até 4.664,68: 22,5% | dedução: R$ 662,77
# Faixa 5: Acima de R$ 4.664,68: 27,5% | dedução: R$ 896