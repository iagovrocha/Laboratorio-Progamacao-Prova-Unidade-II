from __future__ import annotations
import datetime


class Matricula:
    def __init__(self, sistema: Sistema):  # type: ignore
        self.__dataMatricula = datetime.date.today()
        self.__idMatricula = len(sistema.getCadastroAlunos()) + 1

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
            Data da Matrícula: {self.getDataMatricula().strftime('%d/%m/%Y')}
            """)