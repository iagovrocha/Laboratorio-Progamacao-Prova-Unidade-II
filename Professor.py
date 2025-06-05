from __future__ import annotations
from Funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, sistema: Sistema, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, # type: ignore
                  diaNasc: int, sexo: str, matricula: int, setor: str, cargo: str, nivel: str, formacao: str, disciplina: str):
        Funcionario.__init__(self, sistema, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel)
        self.__formacao = formacao
        self.__disciplina  = disciplina
        #sistema.cadastrarProfessor(self)

    def getFormacao(self) -> str:
        return self.__formacao
    
    def getDisciplina(self) -> str:
        return self.__disciplina

    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina

    def setFormacao(self, formacao):
        self.__formacao = formacao

    def Exibir(self):
        Funcionario.Exibir(self)
        print(f"{' Informações Professor ':-^50}")
        print(f"""
            Formação: {self.getFormacao()}
            Disciplina: {self.getDisciplina()}
        """)