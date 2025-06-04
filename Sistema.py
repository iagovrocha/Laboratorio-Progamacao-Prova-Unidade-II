from __future__ import annotations
from Professor import Professor
class Sistema:
    def __init__(self):
        self.__cadastroFuncionarios = {}
        self.__cadastroCoordenadoresAdministrativo = {}
        self.cadastroProfessores = {}
        self.cadastroAlunos = {}
        # self.cadastroCoordenadores = {}
        # self.cadastroCursos = {}
        self.__cadastroMatriculas = {}

    def getCadastroFuncionarios(self) -> dict:
        return self.__cadastroFuncionarios
    def getCoordenadoresAdministrativo (self) -> dict:
        return self.__cadastroCoordenadoresAdministrativo
    def getCadastroProfessor(self) -> dict:
        return self.cadastroProfessores
    def getCadastroAlunos(self) -> dict: 
        return self.cadastroAlunos
    def getCadastroMatriculas(self) -> dict: 
        return self.__cadastroMatriculas
    
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
    def cadastrarProfessor(self) -> bool: # type: ignore
        professor = Professor(self,"jorge","teste","teste",2000,10,11,"m",123,'a','b','c','prof','mat')
        """
        -> Cadastra o obejeto Professor, adicionado ele ao dicionario cadastroProfessor.
        :paramtr Professor: Professor
        :return: True se o Professor foi inserido False caso não
        """
        cadastro = self.cadastroProfessores
        if not professor in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = professor
            return True
        else:
            return False
    def cadastrarAluno(self, aluno: "Aluno") -> bool: # type: ignore
        """
        -> Cadastra o objeto Aluno, adicionando-o ao dicionário cadastroAlunos.
        :paramtr aluno: Aluno
        :return: True se o Aluno foi inserido, False caso contrário
        """
        cadastro = self.cadastroAlunos
        if not aluno in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = aluno
            return True
        else:
            return False

    def cadastrarMatriculas(self, matricula: "Matricula") -> bool: # type: ignore
        """
        -> Cadastra o objeto Matricula, adicionando-o ao dicionário __cadastroMatriculas.
        :paramtr matricula: Matricula
        :return: True se a Matricula foi inserida, False caso contrário
        """
        cadastro = self.__cadastroMatriculas
        if not matricula in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = matricula
            return True
        else:
            return False