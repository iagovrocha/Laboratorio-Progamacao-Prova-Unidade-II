from __future__ import annotations
from Funcionario import Funcionario
from Coordenador import Coordenador
from CoordenadorAdm import CoordenadorAdm
from Professor import Professor
from Aluno import Aluno
from Curso import Curso


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
    
    def cadastrarFuncionario(self) -> bool: # type: ignore
        print("Cadastrado funcionario!!!!!!!!!")
        from CadastroFuncionario import menuCadastroFuncionario
        """
        -> Cadastra o obejeto Funcionario, adicionado ele ao dicionario cadastroFuncionarios.
        :paramtr funcionario: Funcionario
        :return: True se o Funcionario foi inserido False caso não
        """
        CadastroFunc = menuCadastroFuncionario()
        f = Funcionario(self, CadastroFunc[0], CadastroFunc[1], CadastroFunc[2], CadastroFunc[3], CadastroFunc[4], CadastroFunc[5], CadastroFunc[6], CadastroFunc[7],
                     CadastroFunc[8], CadastroFunc[9], CadastroFunc[10])
        cadastro = self.__cadastroFuncionarios
        if not f in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = f
            return True
        else:
            return False
    
    def cadastrarCoordenadoresAdministrativo(self) -> bool: # type: ignore
        print("Cadastrado adm!!!!!!!!!")
        from CadastroCoordenadorAdm import menuCadastroCoordenadorAdm
        """
        -> Cadastra o obejeto CoordenadorAdm, adicionado ele ao dicionario cadastroCoordenadoresAdministrativo.
        :paramtr CoordenadorAdm: CoordenadorAdm
        :return: True se o CoordenadorAdm foi inserido False caso não
        """
        CadastroAdm = menuCadastroCoordenadorAdm()
        coordAdm = CoordenadorAdm(self, CadastroAdm[0], CadastroAdm[1], CadastroAdm[2], CadastroAdm[3], CadastroAdm[4], CadastroAdm[5], CadastroAdm[6], CadastroAdm[7],
                    CadastroAdm[8], CadastroAdm[9], CadastroAdm[10], CadastroAdm[11])
        cadastro = self.__cadastroCoordenadoresAdministrativo
        if not coordAdm in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = coordAdm
            return True
        else:
            return False
    
    def cadastrarProfessor(self) -> bool: # type: ignore
        print("professor!!!!")
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
    def cadastrarAluno(self) -> bool: # type: ignore
        from CadastroAluno import menuCadastroAluno
        print("Cadastrado aluno!!!!!!!!!")
        """
        -> Cadastra o objeto Aluno, adicionando-o ao dicionário cadastroAlunos.
        :paramtr aluno: Aluno
        :return: True se o Aluno foi inserido, False caso contrário
        """
        CadastroAluno = menuCadastroAluno()
        aluno = Aluno(self, CadastroAluno[0], CadastroAluno[1], CadastroAluno[2], CadastroAluno[3], CadastroAluno[4], CadastroAluno[5], CadastroAluno[6], CadastroAluno[7],
               CadastroAluno[8], CadastroAluno[9])
        cadastro = self.__cadastroAlunos
        if not aluno in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = aluno
            return True
        else:
            return False
        
    def cadastrarCoordenador(self) -> bool: # type: ignore
        print("Cadastrado Coordenador!!!!!!!!!")
        from CadastroCoordenador import menuCadastroCoordenador
        """
        -> Cadastra o obejeto Coordenador, adicionado ele ao dicionario cadastroCoordenadores.
        :paramtr Coordenador: Coordenador
        :return: True se o Coordenador foi inserido False caso não
        """
        CadastroCoord = menuCadastroCoordenador()
        coord = Coordenador(self, CadastroCoord[0], CadastroCoord[1], CadastroCoord[2], CadastroCoord[3], CadastroCoord[4], CadastroCoord[5], CadastroCoord[6], CadastroCoord[7],
                     CadastroCoord[8], CadastroCoord[9], CadastroCoord[10], CadastroCoord[11], CadastroCoord[12], CadastroCoord[13])
        cadastro = self.__cadastroCoordenadores
        if not coord in cadastro.values():
            idAtual = len(cadastro) + 1
            cadastro[idAtual] = coord
            return True
        else:
            return False
    
    def cadastrarCurso(self):  # type: ignore
        print("Cadastrado Curso!!!!!!!!!")
        from CadastroCurso import menuCadastroCurso
        """
        -> Cadastra o obejeto Curso, adicionado ele ao dicionario Curso.
        :paramtr Curso: Curso
        :return: True se o Curso foi inserido False caso não
        """
        CadastroCurso = menuCadastroCurso(self)
        curso = Curso(CadastroCurso[0], CadastroCurso[1], CadastroCurso[2], CadastroCurso[3], CadastroCurso[4])
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