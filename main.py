from __future__ import annotations
from Funcionario import Funcionario
from Sistema import Sistema
from Salario import *

if __name__ == "__main__":
    sistema = Sistema()
    funcionario1 = Funcionario(sistema, "NOME FUNCIONARIO", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX", 1993, 11, 11, "Masculino", 1, "Administrativo", "Funcionario Administrativo", 1)
    # print(sistema.cadastroFuncionario(funcionario1))
    print(sistema.cadastroFuncionario(funcionario1))
    print(sistema.getCadastroFuncionarios())
    sistema.getCadastroFuncionarios()[1].Exibir()

    salario = Salario(True, strategy = ProfessorNivelI)
    print(salario.calcularSalario())