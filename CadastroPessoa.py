def getPositiveInt(prompt: str):
    while True:
        try:
            n = int(input(f"{prompt}: "))
            if n <= 0:
                raise ValueError
        except (TypeError, ValueError):
            print("ERRO: O que foi digitado não é um número, ou é inválido.")
        else:
            return n


def menuCadastroPessoa() -> list:
    variaveisCadastros = []
    variaveisCadastros.append(str(input("Nome: ").upper()))
    while True:
        rg = str(input("RG: "))
        if len(rg) != 12:
            print("ERRO: RG inválido")
        else:
            variaveisCadastros.append(rg)
            break
    while True:
        cpf = str(input("CPF: "))
        if len(cpf) != 14:
            print("ERRO: CPF inválido")
        else:
            variaveisCadastros.append(cpf)
            break
    
    variaveisCadastros.append(getPositiveInt("Ano Nascimento"))
    
    while True:
        mes_nascimento = getPositiveInt("Mês Nascimento")
        if mes_nascimento > 12:
            print("ERRO: Mês inválido")
        else:
            variaveisCadastros.append(mes_nascimento)
            break
    while True:
        dia_nascimento = getPositiveInt("Dia Nascimento")
        if dia_nascimento > 31:
            print("ERRO: Dia inválido")
        else:
            variaveisCadastros.append(dia_nascimento)
            break
    
    SEXO_MAP = {
        "M": "MASCULINO",
        "F": "FEMININO"
    }
    while True:
        sexo = str(input("Sexo [M/F]: "))[0].upper()
        if sexo not in "MF":
            print("ERRO: Informação inválida, informe M ou F")
        else:
            variaveisCadastros.append(SEXO_MAP.get(sexo))
            break
    return variaveisCadastros
