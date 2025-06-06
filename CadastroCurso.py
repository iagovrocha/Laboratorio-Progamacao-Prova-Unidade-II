from __future__ import annotations
from CadastroPessoa import getPositiveInt

def escolhaProfessor(sistema):
        
    listaProfessores = sistema.getCadastroProfessores()
    listaCoordenadores = sistema.getCadastroCoordenadores() 
    OPTIONS_MAP_PROFESSOR = {}
    opcoes = 0
    print(f"{' Adcionar Professor ':-^50} ")
    if len(listaProfessores) != 0:
        for professor in listaProfessores.values():
            opcoes += 1
            print(f"      {opcoes}. {professor.getNome()} - {professor.getFormacao()} - {professor.getDisciplina()}")
            OPTIONS_MAP_PROFESSOR[opcoes] = professor
    else:
        print("Não há professores cadastrados.")

    if len(listaCoordenadores) != 0:
        for coordenador in listaCoordenadores.values():
            opcoes += 1
            print(f"      {opcoes}. {coordenador.getNome()} - {coordenador.getFormacao()} - {coordenador.getDisciplina()}")
            OPTIONS_MAP_PROFESSOR[opcoes] = coordenador
    else:
        print("Não há coordenadores cadastrados.")
    print("-"*50)
    while True:
        if len(listaCoordenadores) != 0 or len(listaProfessores) != 0:
            try:
                opcao = int(input("Opção: "))
                if opcao <= 0 or opcao > opcoes:
                    raise TypeError
                return OPTIONS_MAP_PROFESSOR.get(opcao)
            except (TypeError, ValueError):
                print("ERRO: O que foi digitado não é um número da opção")
        else:
            return "NENHUM COORDENADOR OU PROFESSOR CADASTRADO"

def escolhaCoordenador(sistema):
    listaCoordenadores = sistema.getCadastroCoordenadores() 

    print(f"{' Adcionar Coordenador ':-^50} ")
    if len(listaCoordenadores) != 0:
        for id, coordenador in listaCoordenadores.items():
            print(f"      {id}. {coordenador.getNome()} - {coordenador.getFormacao()} - {coordenador.getDisciplina()}")
    else:
        print("Não há coordenadores cadastrados.")
        return "NENHUM COORDENADOR CADASTRADO"
    print("-"*50)
    while True:
        try:
            opcao = int(input("Opção: "))
            if opcao <= 0 or opcao > len(listaCoordenadores):
                raise TypeError
            return listaCoordenadores.get(opcao)
        except (TypeError, ValueError):
            print("ERRO: O que foi digitado não é um número da opção")
    

def menuCadastroCurso(sistema: Sistema): # type: ignore
    variaveisCadastros = []
    variaveisCadastros.append(str(input("Titulo: ")).title())
    variaveisCadastros.append(str(input("Descrição: ")))
    variaveisCadastros.append(str(input("Sala: ")))
    
    variaveisCadastros.append(escolhaProfessor(sistema))
    variaveisCadastros.append(escolhaCoordenador(sistema))
    
    return variaveisCadastros 
