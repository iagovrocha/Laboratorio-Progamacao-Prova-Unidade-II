from CadastroProfessor import menuCadastroFuncionario

def menuCadastroCoordenadorAdm():
    variaveisCadastros = menuCadastroFuncionario()
    variaveisCadastros.append(str(input("Área: ")).upper())

    return variaveisCadastros