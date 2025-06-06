from CadastroProfessor import menuCadastroProfessor

def menuCadastroCoordenador():
    variaveisCadastros = menuCadastroProfessor()
    variaveisCadastros.append(str(input("Área: ")).upper())

    return variaveisCadastros