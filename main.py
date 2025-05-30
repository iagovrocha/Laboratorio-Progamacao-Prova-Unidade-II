from __future__ import annotations
from Funcionario import Funcionario
from CoordenadorAdm import CoordenadorAdm
from Sistema import Sistema
from Salario import *
from Aluno import Aluno


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

    print("\n--- Testando a classe Aluno ---")
    aluno1 = Aluno(sistema, "Maria Silva", "12.345.678-9", "123.456.789-00", 2005, 3, 15, "Feminino", 1001, "Ciência de Dados", 150.00)
    print(f"Aluno cadastrado: {sistema.cadastrarAluno(aluno1)}") # Deve retornar False, pois o cadastro já ocorreu no construtor
    print("Cadastro de Alunos no Sistema:", sistema.getCadastroAlunos())
    if sistema.getCadastroAlunos(): # Adicionado verificação para evitar erro se estiver vazio
        sistema.getCadastroAlunos()[1].Exibir()

    aluno2 = Aluno(sistema, "João Souza", "98.765.432-1", "987.654.321-99", 2004, 7, 20, "Masculino", 1002, "Engenharia de Software", 0.00)
    print(f"Aluno cadastrado: {sistema.cadastrarAluno(aluno2)}")
    print("Cadastro de Alunos no Sistema (após segundo aluno):", sistema.getCadastroAlunos())
    if sistema.getCadastroAlunos() and 2 in sistema.getCadastroAlunos():
        sistema.getCadastroAlunos()[2].Exibir()