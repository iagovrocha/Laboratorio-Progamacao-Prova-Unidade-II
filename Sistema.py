from __future__ import annotations

from Professor import Professor


class Sistema:
    def __init__(self):
        self.__cadastroFuncionarios = {}
        self.__cadastroCoordenadoresAdministrativo = {}
        self.__cadastroProfessores = {}
        self.__cadastroAlunos = {}
        self.__cadastroCoordenadores = {}
        self.__cadastroCursos = {}
        # self.__cadastroMatriculas = {}

    def getCadastroFuncionarios(self) -> dict:
        return self.__cadastroFuncionarios
    
    def getCoordenadoresAdministrativo(self) -> dict:
        return self.__cadastroCoordenadoresAdministrativo
    
    def getCadastroProfessores(self) -> dict:
        return self.__cadastroProfessores
    
    def getCadastroAlunos(self) -> dict: 
        return self.__cadastroAlunos
    
    def getCadastroCoordenadores(self) -> dict:
        return self.__cadastroCoordenadores
    
    def getCadastroCursos(self):
        return self.__cadastroCursos
    # def getCadastroMatriculas(self) -> dict: 
    #     return self.__cadastroMatriculas
    
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
        from CadastroProfessor import menuCadastroProfessor

        """
        -> Cadastra o obejeto Professor, adicionado ele ao dicionario cadastroProfessor.
        :paramtr Professor: Professor
        :return: True se o Professor foi inserido False caso não
        """
        CadastroProf = menuCadastroProfessor()
        professor = Professor(self, CadastroProf[0], CadastroProf[1], CadastroProf[2], CadastroProf[3], CadastroProf[4], CadastroProf[5], CadastroProf[6], CadastroProf[7],
            CadastroProf[8], CadastroProf[9], CadastroProf[10], CadastroProf[11], CadastroProf[12])
        cadastro = self.__cadastroProfessores
        if not professor in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = professor
            print("Professor cadastrado.")
            return True
        else:
            return False
    def cadastrarAluno(self, aluno: Aluno) -> bool: # type: ignore
        """
        -> Cadastra o objeto Aluno, adicionando-o ao dicionário cadastroAlunos.
        :paramtr aluno: Aluno
        :return: True se o Aluno foi inserido, False caso contrário
        """
        cadastro = self.__cadastroAlunos
        if not aluno in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = aluno
            return True
        else:
            return False
        
    def cadastrarCoordenador(self, coordenador: Coordenador) -> bool: # type: ignore
        """
        -> Cadastra o obejeto Coordenador, adicionado ele ao dicionario cadastroCoordenadores.
        :paramtr Coordenador: Coordenador
        :return: True se o Coordenador foi inserido False caso não
        """
        cadastro = self.__cadastroCoordenadores
        if not coordenador in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = coordenador
            return True
        else:
            return False
    
    def cadastrarCurso(self, curso: Curso):  # type: ignore
        """
        -> Cadastra o obejeto Curso, adicionado ele ao dicionario Curso.
        :paramtr Curso: Curso
        :return: True se o Curso foi inserido False caso não
        """
        cadastro = self.__cadastroCursos
        if not curso in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = curso
            return True
        else:
            return False

    # def cadastrarMatriculas(self, matricula: "Matricula") -> bool: # type: ignore
    #     """
    #     -> Cadastra o objeto Matricula, adicionando-o ao dicionário __cadastroMatriculas.
    #     :paramtr matricula: Matricula
    #     :return: True se a Matricula foi inserida, False caso contrário
    #     """
    #     cadastro = self.__cadastroMatriculas
    #     if not matricula in cadastro.values():
    #         idAtual = len(cadastro) + 1
    #         cadastro[idAtual] = matricula
    #         return True
    #     else:
    #         return False