from __future__ import annotations
class Sistema:
    def __init__(self):
        self.cadastroFuncionarios = {}
        # self.cadastroProfessores = {}
        # self.cadastroAlunos = {}
        # self.cadastroCoordenadores = {}
        # self.cadastroCoordenadoresAdministrativo = {}
        # self.cadastroCursos = {}

    def cadastroFuncionario(self, funcionario: "Funcionario"):
        cadastro = self.cadastroFuncionarios
        idAtual = len(cadastro) + 1
        cadastro[idAtual] = funcionario