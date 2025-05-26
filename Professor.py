from __future__ import annotations
from Funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, sistema, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel, formacao, disciplina):
        Funcionario.__init__(self, sistema, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel)
        self.__formacao = formacao
        self.__disciplina  = disciplina
        

    def getFormacao(self) -> str:
        return self.__formacao
    
    def getDisciplina(self) -> str:
        return self.__disciplina

    def Exibir(self):
        Funcionario.Exibir()
        print(f"{' Informações Professor ':-^50}")
        print(f"Formação: {self.getFormacao()}")  
        print(f"Disciplina: {self.getDisciplina()}")

    def CadastrarProfessor(self):
        pass ##adicionarei futuramente