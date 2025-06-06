from Funcionario import Funcionario
from Coordenador import Coordenador
from CoordenadorAdm import CoordenadorAdm
from Professor import Professor
from Aluno import Aluno
from Curso import Curso
from Sistema import Sistema

if __name__ == "__main__":
    from CadastroFuncionario import menuCadastroFuncionario
    from CadastroProfessor import menuCadastroProfessor
    from CadastroCoordenador import menuCadastroCoordenador
    from CadastroCoordenadorAdm import menuCadastroCoordenadorAdm
    from CadastroAluno import menuCadastroAluno
    from CadastroCurso import menuCadastroCurso

    sistema = Sistema()
    """Funciona"""
    # CadastroFunc = menuCadastroFuncionario()
    # print(CadastroFunc)
    # print(len(CadastroFunc))
    # f = Funcionario(sistema, CadastroFunc[0], CadastroFunc[1], CadastroFunc[2], CadastroFunc[3], CadastroFunc[4], CadastroFunc[5], CadastroFunc[6], CadastroFunc[7],
    #                 CadastroFunc[8], CadastroFunc[9], CadastroFunc[10])
    # f.Exibir()

    """Funciona"""
    # CadastroAdm = menuCadastroCoordenadorAdm()
    # coordAdm = CoordenadorAdm(sistema, CadastroAdm[0], CadastroAdm[1], CadastroAdm[2], CadastroAdm[3], CadastroAdm[4], CadastroAdm[5], CadastroAdm[6], CadastroAdm[7],
    #                 CadastroAdm[8], CadastroAdm[9], CadastroAdm[10], CadastroAdm[11])

    # coordAdm.Exibir()

    """Funciona"""
    # CadastroProf = menuCadastroProfessor()
    # prof = Professor(sistema, CadastroProf[0], CadastroProf[1], CadastroProf[2], CadastroProf[3], CadastroProf[4], CadastroProf[5], CadastroProf[6], CadastroProf[7],
    #         CadastroProf[8], CadastroProf[9], CadastroProf[10], CadastroProf[11], CadastroProf[12])

    # prof.Exibir()

    """Funciona"""
    # CadastroCoord = menuCadastroCoordenador()
    # coord = Coordenador(sistema, CadastroCoord[0], CadastroCoord[1], CadastroCoord[2], CadastroCoord[3], CadastroCoord[4], CadastroCoord[5], CadastroCoord[6], CadastroCoord[7],
    #                 CadastroCoord[8], CadastroCoord[9], CadastroCoord[10], CadastroCoord[11], CadastroCoord[12], CadastroCoord[13])

    # coord.Exibir()

    """Funciona"""
    # CadastroAluno = menuCadastroAluno()
    # aluno = Aluno(sistema, CadastroAluno[0], CadastroAluno[1], CadastroAluno[2], CadastroAluno[3], CadastroAluno[4], CadastroAluno[5], CadastroAluno[6], CadastroAluno[7],
    #           CadastroAluno[8], CadastroAluno[9])
    # aluno.Exibir()

    # professor = Professor(sistema, "NOME PROF", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX",1993,11,11,"Masculino", 1, "Administrativo", "Funcionario Administrativo", "III", "FORMACAO", "DISCIPLINA")
    # coordenador = Coordenador(sistema, "NOME COORDENADOR", "XX.XXX.XXX-X", "XXX.XXX.XXX-XX", 1993, 11, 11, "Masculino", 1, "Administrativo", "Funcionario Administrativo", "III", "FORMACAO", "DISCIPLINA", "AREA")
    
    """Funciona"""
    # print(sistema.getCadastroCoordenadores())
    # print(sistema.getCadastroProfessores())
    # CadastroCurso = menuCadastroCurso(sistema)
    # curso = Curso(CadastroCurso[0], CadastroCurso[1], CadastroCurso[2], CadastroCurso[3], CadastroCurso[4])
    # curso.Exibir()