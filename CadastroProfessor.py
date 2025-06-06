from CadastroFuncionario import menuCadastroFuncionario

def menuCadastroProfessor():
    variaveisCadastros = menuCadastroFuncionario(True)

    variaveisCadastros.append(str(input("Formação: ")).upper())
    variaveisCadastros.append(str(input("Diciplina: ")).upper())
    return variaveisCadastros

if __name__ == "__main__":
    # professor = Professor(self, "NOME PROF", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX",1993,11,11,"Masculino", 1, "Administrativo", "Funcionario Administrativo", "A", "FORMACAO", "DISCIPLINA")
    menuCadastroProfessor()
