from Professor import Professor
from Coordenador import Coordenador

class Curso:

    #Construtor da Classe Curso
    def __init__(self,titulo :str,descricao :str,sala :str,idCurso :int, professor :Professor, coordenador :Coordenador):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__valor = 865.23
        self.sala = sala
        self.__idCurso = idCurso 
        self.professor = professor
        self.coordenador = coordenador 
        self.numMinAluno = None

    def cadastrarCurso():
        #Vai ficar faltando
        return 
    
    def exibirCurso(self) -> str:
        return f"""
        Curso: {self.__titulo}
        Descrição: {self.__descricao}
        Custo: {self.__valor}
        Sala: {self.sala}
        ID: {self.__idCurso}
        Professor: {self.professor}
        Coordenador: {self.coordenador}
        Numero Minimo de Alunos: {self.numMinAluno}

        """
    
    def calcularNumMinAluno(self) -> int:
        self.numMinAluno = self.professor.getSalario()/self.__valor
        return int(f"{self.numMinAluno:.0f}")