from __future__ import annotations
class Sistema:
    def __init__(self):
        self.__cadastroFuncionarios = {}
        # self.cadastroProfessores = {}
        # self.cadastroAlunos = {}
        # self.cadastroCoordenadores = {}
        # self.cadastroCoordenadoresAdministrativo = {}
        # self.cadastroCursos = {}

    def getCadastroFuncionarios(self) -> dict:
        return self.__cadastroFuncionarios

    def cadastroFuncionario(self, funcionario: "Funcionario") -> bool: # type: ignore
        """
        -> Cadastra o obejeto Funcionario, adicionado ele ao dicionario cadastroFuncionarios.
        :paramtr funcionario: Funcionario
        :return: True se o Funcionario foi inserido False caso não
        """
        cadastro = self.__cadastroFuncionarios
        if not funcionario in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = funcionario
            return True
        else:
            return False