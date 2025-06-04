from __future__ import annotations
from Funcionario import Funcionario
from CoordenadorAdm import CoordenadorAdm
from Professor import Professor
from Sistema import Sistema
from Salario import *


def testes():
    sistema = Sistema()
    funcionario1 = Funcionario(sistema, "NOME FUNCIONARIO", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX", 1993, 11, 11, "Masculino", 1, "Administrativo", "Funcionario Administrativo", "A")
    print(sistema.cadastrarFuncionario(funcionario1))
    print(sistema.getCadastroFuncionarios())
    sistema.getCadastroFuncionarios()[1].Exibir()

    salario = Salario(strategy = TecnicoAdministrativoE)
    print(salario.getSalarioLiquido())
    coordenadorAdm01 = CoordenadorAdm(sistema, "NOME COORDENADOR", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX", 1993, 11, 11, "Masculino", 1, "Administrativo", "Funcionario Administrativo", "E", "RH")
    print(sistema.getCoordenadoresAdministrativo()[1].get_nome())
    print(sistema.getCoordenadoresAdministrativo()[1].calcularPlusSalario())
    sistema.getCoordenadoresAdministrativo()[1].Exibir()

    
    coordenadorAdm01.setNivel("D")
    print(sistema.getCoordenadoresAdministrativo()[1].getSalario().getSalarioLiquido())
    print(sistema.getCoordenadoresAdministrativo()[1].calcularPlusSalario())
    sistema.getCoordenadoresAdministrativo()[1].Exibir()


    professor = Professor(sistema, "NOME PROF", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX",1993,11,11,"Masculino", 1, "Administrativo", "Funcionario Administrativo", "A", "FORMACAO", "DISCIPLINA")
    print(sistema.cadastrarProfessor(professor))
    print(sistema.getCadastroProfessor())
    sistema.getCadastroProfessor()[1].Exibir()

def escolherClasse() -> str:
    mapeamentoClasses = {
        1 : "Aluno",
        2 : "Professor",
        3 : "Coordenador",
        4 : "Coordenador Adm",
        5 : "Curso"
    }

    print("""
        +--------- CLASSE ---------+
        |                          |
        |      1) Aluno            |
        |      2) Professor        |
        |      3) Coordenador      |
        |      4) Coordenador Adm  |
        |      5) Curso            |
        |                          |
        +--------------------------+
""")    
    classe = mapeamentoClasses[int(input("Escolha sua classe: "))]
    return classe

def adicionar(sistema :Sistema, classe) -> dict[str,any]:
    mapeamentoClasses = {
        "Aluno": sistema,
        "Professor":sistema.cadastrarProfessor(),
        "Coordenador": sistema,
        "Coordenador Adm":sistema,
        "Curso": sistema
    }

    return mapeamentoClasses[classe]

    
def exibir(sistema :Sistema,classe):
    mapeamentoClasses = {
        "Aluno": sistema,
        "Professor":sistema.getCadastroProfessor(),
        "Coordenador": sistema,
        "Coordenador Adm": sistema,
        "Curso": sistema
    }
    print(mapeamentoClasses[classe])
    print("""
        +--------- EXIBIR ---------+
        |                          |
        |      1) Apenas um (id)   |
        |      2) Todos            |
        |                          |
        +--------------------------+

""")
    r = int(input("Escolha a opçao: "))
    if r == 1:
        mapeamentoClasses[classe][int(input("Digite o ID: "))].Exibir()
    elif r == 2:
        for c in mapeamentoClasses[classe].keys():
            print(f"\n======================= ID: {c} =======================\n")
            mapeamentoClasses[classe][c].Exibir()
        

def menu() -> None:
    try:
        sistema = Sistema()
        while True:
            print("""
        +--------- MENU ---------+
        |                        |
        |      1) Adicionar      |
        |      2) Exibir         |
        |      3) Cancelar       |
        |                        |
        +------------------------+
                """)
            resp = int(input("Escolha uma opção: "))
            if resp == 3:
                print("Parando sistema...")
                break
            elif resp == 1:
                c = escolherClasse()
                adicionar(sistema,c)
            elif resp == 2:
                c = escolherClasse()
                exibir(sistema,c)

    except KeyboardInterrupt:
        print("Parando sistema...")

if __name__ == "__main__":
    menu()