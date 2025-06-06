from CadastroPessoa import menuCadastroPessoa, getPositiveInt

def menuCadastroAluno():
    variaveisCadastros = menuCadastroPessoa()
    variaveisCadastros.append(getPositiveInt("Codigo"))
    variaveisCadastros.append(str(input("Interesse: ")))
    while True:
        try:
            desconto = float(input("Desconto %: "))
        except (TypeError, ValueError):
            print("ERRO: O que foi digitado é inválido")
        else:
            variaveisCadastros.append(desconto / 100)
            break
    
    return variaveisCadastros

