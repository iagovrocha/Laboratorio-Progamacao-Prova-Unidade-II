from __future__ import annotations
class Curso:

    #Construtor da Classe Curso
    def __init__(self, titulo: str, descricao: str, sala: str, professor: Professor, coordenador: Coordenador): # type: ignore
        self.__titulo = titulo
        self.__descricao = descricao
        self.__valor = 865.23
        self.sala = sala
        self.professor = professor
        self.coordenador = coordenador 
        self.numMinAluno = None

    def getTitulo(self) -> str:
        return self.__titulo
    
    def getDescricao(self) -> str:
        return self.__descricao
    
    def getValor(self) -> float:
        return self.__valor

    def cadastrarCurso():
        #Vai ficar faltando
        return 
    
    def Exibir(self):
        print(f"{' Informações Curso ':-^50}")
        print(f"""
            Curso: {self.getTitulo()}
            Descrição: {self.getDescricao()}
            Custo: {self.getValor()}
            Sala: {self.sala}
            Professor: {self.professor.getNome()}
            Coordenador: {self.coordenador.getNome()}
            Numero Minimo de Alunos: {self.numMinAluno}
        """)
    
    def calcularNumMinAluno(self) -> int:
        self.numMinAluno = self.professor.getSalario() / self.__valor
        return int(f"{self.numMinAluno:.0f}")