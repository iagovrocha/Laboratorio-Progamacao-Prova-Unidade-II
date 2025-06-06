from __future__ import annotations
from Pessoa import Pessoa

from Matricula import Matricula
class Aluno(Pessoa):
    def __init__(self, sistema: Sistema, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, # type: ignore
                  diaNasc: int, sexo: str, codigo: int, interesse: str, desconto: float, matricula : Matricula):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo)
        self.__codigo = codigo
        self.__interesse = interesse
        self.__desconto = desconto
        self.__matricula = Matricula()
        

    def getCodigo(self) -> int:
        return self.__codigo

    def getInteresse(self) -> str:
        return self.__interesse

    def getDesconto(self) -> float:
        return self.__desconto

    def getMatricula(self) -> Matricula:
        return self.__matricula
    
    def setInteresse(self, interesse: str):
        self.__interesse = interesse

    def setDesconto(self, desconto: float):
        self.__desconto = desconto

    def Exibir(self):
        super().Exibir()
        print(f"{' Informações Aluno ':-^50}")
        print(f"""
            Código: {self.getCodigo()}
            Interesse: {self.getInteresse()}
            Desconto: R${self.getDesconto():.2f}
            Matricula: {self.getMatricula().getIdMatricula()}
            """)
