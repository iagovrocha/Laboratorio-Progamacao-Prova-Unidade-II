from Funcionario import Funcionario
from Sistema import Sistema

if __name__ == "__main__":
    sistema = Sistema()
    funcionario1 = Funcionario(sistema, "NOME FUNCIONARIO", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX", 1993, 11, 11, "Masculino", 1, "Administrativo", "Funcionario Administrativo", 1)
    sistema.cadastroFuncionario(funcionario1)
    print(sistema.cadastroFuncionario(funcionario1))
    print(sistema.cadastroFuncionarios)
    sistema.cadastroFuncionarios[1].Exibir()