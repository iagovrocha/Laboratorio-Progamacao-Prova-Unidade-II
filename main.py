from __future__ import annotations
from Funcionario import Funcionario
from CoordenadorAdm import CoordenadorAdm
from Professor import Professor
from Sistema import Sistema
from Aluno import Aluno
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

    aluno1 = Aluno(sistema, "Maria Silva", "12.345.678-9", "123.456.789-00", 2005, 3, 15, "Feminino", 1001, "Ciência de Dados", 150.00)
    if sistema.getCadastroAlunos(): 
        sistema.getCadastroAlunos()[1].Exibir()

    aluno2 = Aluno(sistema, "João Souza", "98.765.432-1", "987.654.321-99", 2004, 7, 20, "Masculino", 1002, "Engenharia de Software", 0.00)
    if sistema.getCadastroAlunos() and 2 in sistema.getCadastroAlunos():
        sistema.getCadastroAlunos()[2].Exibir()

def main():
    try:
        resp = 0
        while resp != 3:
            print("""
        ---------- MENU ----------
        |                        |
        |     1) Adicionar       |
        |     2) Exibir          |
        |     3) Cancelar        |
        |                        |
        --------------------------
                """)
            resp = int(input("Escolha uma opção: "))
            if resp == 3:
                print("Parando sistema...")
                break
            elif resp == 1:
                print("Adicionar")
            elif resp == 2:
                print("Exibir")
    except KeyboardInterrupt:
        print("Parando sistema...")
if __name__ == "__main__":
    main()