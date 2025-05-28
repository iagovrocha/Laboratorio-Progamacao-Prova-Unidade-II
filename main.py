from __future__ import annotations
from Funcionario import Funcionario
from CoordenadorAdm import CoordenadorAdm
from Sistema import Sistema
from Salario import *

if __name__ == "__main__":
    sistema = Sistema()
    funcionario1 = Funcionario(sistema, "NOME FUNCIONARIO", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX", 1993, 11, 11, "Masculino", 1, "Administrativo", "Funcionario Administrativo", "A")
    # print(sistema.cadastroFuncionario(funcionario1))
    print(sistema.cadastrarFuncionario(funcionario1))
    print(sistema.getCadastroFuncionarios())
    sistema.getCadastroFuncionarios()[1].Exibir()

    salario = Salario(strategy = TecnicoAdministrativoE)
    print(salario.getSalarioLiquido())
    coordenadorAdm01 = CoordenadorAdm(sistema, "NOME COORDENADOR", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX", 1993, 11, 11, "Masculino", 1, "Administrativo", "Funcionario Administrativo", "E", "RH")
    print(sistema.getCoordenadoresAdministrativo()[1].get_nome())
    print(sistema.getCoordenadoresAdministrativo()[1].calcularPlusSalario())
    sistema.getCoordenadoresAdministrativo()[1].Exibir()