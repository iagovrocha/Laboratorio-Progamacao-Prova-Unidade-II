from __future__ import annotations
class Sistema:
    def __init__(self):
        self.__cadastroFuncionarios = {}
        self.__cadastroCoordenadoresAdministrativo = {}
        # self.cadastroProfessores = {}
        self.__cadastroAlunos = {}
        # self.cadastroCoordenadores = {}
        # self.cadastroCursos = {}

    def getCadastroFuncionarios(self) -> dict:
        return self.__cadastroFuncionarios
    def getCoordenadoresAdministrativo (self) -> dict:
        return self.__cadastroCoordenadoresAdministrativo
    def getCadastroAlunos(self) -> dict: 
        return self.__cadastroAlunos

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
        
    def cadastrarAluno(self, aluno: "Aluno") -> bool: # type: ignore
        """
        -> Cadastra o objeto Aluno, adicionando-o ao dicionário cadastroAlunos.
        :paramtr aluno: Aluno
        :return: True se o Aluno foi inserido False caso não
        """
        cadastro = self.__cadastroAlunos
        if not aluno in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = aluno
            return True
        else:
            return False

    