from __future__ import annotations
import datetime
from Aluno import Aluno
from Curso import Curso


class Matricula:
    def __init__(self, sistema: Sistema, aluno: Aluno, curso: Curso):  # type: ignore
        self.__aluno = aluno
        self.__curso = curso
        self.__dataMatricula = datetime.date.today()
        self.__idMatricula = len(sistema.getCadastroAlunos()) + 1

    def getAluno(self) -> Aluno: 
        return self.__aluno

    def getCurso(self) -> Curso: 
        return self.__curso

    def getDataMatricula(self) -> datetime.date:
        return self.__dataMatricula

    def getIdMatricula(self) -> int:
        return self.__idMatricula

    def __str__(self) -> str:
        return f"Matricula(ID: {self.getIdMatricula()}, Aluno: {self.getAluno().getNome()}, Curso: {self.getCurso().getTitulo()}, Data: {self.getDataMatricula()})"

    def Exibir(self):
        print(f"{' Informações da Matrícula ':-^50}")
        print(f"""
            ID da Matrícula: {self.getIdMatricula()}
            Aluno: {self.getAluno().getNome()} (Código: {self.getAluno().getCodigo()})
            Curso: {self.getCurso().getTitulo()} (ID: {self.getCurso().getId()})
            Data da Matrícula: {self.getDataMatricula().strftime('%d/%m/%Y')}
            """)