from __future__ import annotations

# Usando Strategy Desing Partter
class Salario:
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

    def setPlanoSaude(self, planoSaude):
        self.__planoSaude = planoSaude

    def calcularSalario(self) -> float:
        if self._strategy:
            self.__salarioBruto = self._strategy.salario()
            # Calculo INSS
            if self.getSalarioBruto() <= 1518:
                self.__inss = self.getSalarioBruto() * 0.075
            elif self.getSalarioBruto() <= 2793.88:
                self.__inss = self.getSalarioBruto() * 0.09
            elif self.getSalarioBruto() <= 4190.3:
                self.__inss = self.getSalarioBruto() * 0.12
            elif self.getSalarioBruto() <= 8157.41:
                self.__inss = self.getSalarioBruto() * 0.14
            else:
                self.__inss = 8157.41 * 0.14
            # Calculo IRRF
            if self.getSalarioBruto() <= 2259.20:
                self.__irrf = 0.0
            elif self.getSalarioBruto() <= 2826.65:
                self.__irrf = self.getSalarioBruto() * 0.075
            elif self.getSalarioBruto() <= 3751.05:
                self.__irrf = self.getSalarioBruto() * 0.15
            elif self.getSalarioBruto() <= 4664.68:
                self.__irrf = self.getSalarioBruto() * 0.225
            else:
                self.__irrf = self.getSalarioBruto() * 0.275

            self.__salarioLiquido = self.getSalarioBruto() - self.getINSS() - self.getIRRF() - self.getPlanoSaude()
            return self.getSalarioLiquido()


class ProfessorNivelI:
    def salario():
        return 4530
class ProfessorNivelII:
    def salario():
        return 5325.50
class ProfessorNivelIII:
    def salario():
        return 8568.43

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
    