from __future__ import annotations
class Sistema:
    def __init__(self):
        self.__cadastroFuncionarios = {}
        self.__cadastroCoordenadoresAdministrativo = {}
        # self.cadastroProfessores = {}
        # self.cadastroAlunos = {}
        # self.cadastroCoordenadores = {}
        # self.cadastroCursos = {}

    def getCadastroFuncionarios(self) -> dict:
        return self.__cadastroFuncionarios
    def getCoordenadoresAdministrativo (self) -> dict:
        return self.__cadastroCoordenadoresAdministrativo

    def cadastrarFuncionario(self, funcionario: "Funcionario") -> bool: # type: ignore
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
    
    def cadastrarCoordenadoresAdministrativo(self, coordnadorAdm: CoordenadorAdm) -> bool: # type: ignore
        """
        -> Cadastra o obejeto CoordenadorAdm, adicionado ele ao dicionario cadastroCoordenadoresAdministrativo.
        :paramtr CoordenadorAdm: CoordenadorAdm
        :return: True se o CoordenadorAdm foi inserido False caso não
        """
        cadastro = self.__cadastroCoordenadoresAdministrativo
        if not coordnadorAdm in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = coordnadorAdm
            return True
        else:
            return False