from __future__ import annotations
from Sistema import Sistema


def escolherClasse() -> str:
    mapeamentoClasses = {
        1 : "Aluno",
        2 : "Professor",
        3 : "Coordenador",
        4 : "Coordenador Adm",
        5 : "Curso",
        6 : "Funcionario"
    }

    print("""
        +--------- CLASSE ---------+
        |                          |
        |      1) Aluno            |
        |      2) Professor        |
        |      3) Coordenador      |
        |      4) Coordenador Adm  |
        |      5) Curso            |
        |      6) Funcionário      |
        |                          |
        +--------------------------+
""")
    classe = mapeamentoClasses[int(input("Escolha sua classe: "))]
    print(classe)
    return classe


def adicionar(sistema :Sistema, classe) -> dict[str,any]:
    mapeamentoClasses = {
        "Aluno": sistema.cadastrarAluno,
        "Professor":sistema.cadastrarProfessor,
        "Coordenador": sistema.cadastrarCoordenador,
        "Coordenador Adm":sistema.cadastrarCoordenadoresAdministrativo,
        "Curso": sistema.cadastrarCurso,
        "Funcionario" : sistema.cadastrarFuncionario
    }
 
    return mapeamentoClasses[classe]()

    
def exibir(sistema :Sistema,classe):
    mapeamentoClasses = {
        "Aluno": sistema.getCadastroAlunos,
        "Professor":sistema.getCadastroProfessores,
        "Coordenador": sistema.getCadastroCoordenadores,
        "Coordenador Adm": sistema.getCoordenadoresAdministrativo,
        "Curso": sistema.getCadastroCursos,
        "Funcionario" : sistema.getCadastroFuncionarios
    }

    print("""
        +--------- EXIBIR ---------+
        |                          |
        |      1) Apenas um (id)   |
        |      2) Todos            |
        |                          |
        +--------------------------+

""")
    r = int(input("Escolha a opçao: "))
    cadastro = mapeamentoClasses[classe]()
    if r == 1:
        cadastro[int(input("Digite o ID: "))].Exibir()
    elif r == 2:
        print(cadastro)
        for c in cadastro.keys():
            print(f"\n======================= ID: {c} =======================\n")
            cadastro[c].Exibir()
    else:
        print("Opção inválida")
        

def menu() -> None:
    sistema = Sistema()
    while True:
        try:
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
            else:
                print("Opção Inválida!!")

        except KeyboardInterrupt:
            print("\nParando sistema...")
            break

        except ValueError:
            print("\nOpção inválida!!")

        except KeyError:
            print("\nOpção inválida \nOperação Cancelada!")




if __name__ == "__main__":
    menu()