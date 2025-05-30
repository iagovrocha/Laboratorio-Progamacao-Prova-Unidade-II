from __future__ import annotations
from Funcionario import Funcionario
from CoordenadorAdm import CoordenadorAdm
from Professor import Professor
from Sistema import Sistema
from Salario import *


def testes():
    sistema = Sistema()
    funcionario1 = Funcionario(sistema, "NOME FUNCIONARIO", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX", 1993, 11, 11, "Masculino", 1, "Administrativo", "Funcionario Administrativo", "A")
    print(sistema.cadastrarFuncionario(funcionario1))
    print(sistema.getCadastroFuncionarios())
    sistema.getCadastroFuncionarios()[1].Exibir()

    salario = Salario(strategy = TecnicoAdministrativoE)
    print(salario.getSalarioLiquido())
    coordenadorAdm01 = CoordenadorAdm(sistema, "NOME COORDENADOR", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX", 1993, 11, 11, "Masculino", 1, "Administrativo", "Funcionario Administrativo", "E", "RH")
    print(sistema.getCoordenadoresAdministrativo()[1].get_nome())
    print(sistema.getCoordenadoresAdministrativo()[1].calcularPlusSalario())
    sistema.getCoordenadoresAdministrativo()[1].Exibir()

    
    coordenadorAdm01.setNivel("D")
    print(sistema.getCoordenadoresAdministrativo()[1].getSalario().getSalarioLiquido())
    print(sistema.getCoordenadoresAdministrativo()[1].calcularPlusSalario())
    sistema.getCoordenadoresAdministrativo()[1].Exibir()


    professor = Professor(sistema, "NOME PROF", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX",1993,11,11,"Masculino", 1, "Administrativo", "Funcionario Administrativo", "A", "FORMACAO", "DISCIPLINA")
    print(sistema.cadastrarProfessor(professor))
    print(sistema.getCadastroProfessor())
    sistema.getCadastroProfessor()[1].Exibir()
def main():
    pass

if __name__ == "__main__":
    testes()