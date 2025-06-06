from CadastroPessoa import *

def menuEscolhasProfessor() -> str:
    ESCOLHAS_MAP = {
        1: "I",
        2: "II",
        3: "III"
    }
    while True:
        print(f"{' Nivel ':-^50}")
        print(f"""
        [1] - Professor Nivel I
        [2] - Professor Nivel II
        [3] - Professor Nivel III
        
{'-'*50}""")
        try:
            opcao = int(input("Opção: "))
            if opcao <= 0 or opcao > 3:
                raise TypeError
            return ESCOLHAS_MAP.get(opcao)
        except (TypeError, ValueError):
            print("ERRO: O que foi digitado não é um número da opção")

def menuEscolhasFuncionario() -> str:
    ESCOLHAS_MAP = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E"
    }
    while True:
        print(f"{' Nivel ':-^50}")
        print(f"""
    [1] - Tecnico Administrativo Nivel A
    [2] - Tecnico Administrativo Nivel B
    [3] - Tecnico Administrativo Nivel C
    [4] - Tecnico Administrativo Nivel D
    [5] - Tecnico Administrativo Nivel E
              
{'-'*50}""")
        try:
            opcao = int(input("Opção: "))
            if opcao <= 0 or opcao > 5:
                raise TypeError
            return ESCOLHAS_MAP.get(opcao)
        except (TypeError, ValueError):
            print("ERRO: O que foi digitado não é um número da opção")

def menuCadastroFuncionario(professor: bool = False) -> list:
    variaveisCadastros = menuCadastroPessoa()
    variaveisCadastros.append(getPositiveInt("Matricula"))
    variaveisCadastros.append(str(input("Setor: ")))
    variaveisCadastros.append(str(input("Cargo: ")))
    if professor:
        variaveisCadastros.append(menuEscolhasProfessor())
    else:
        variaveisCadastros.append(menuEscolhasFuncionario())

    return variaveisCadastros