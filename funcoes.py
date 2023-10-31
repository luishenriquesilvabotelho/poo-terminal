from classes import *

def cadastrar_aluno(nomec, sexoc, matriculac, senhac, turmac):
    aluno = Aluno(nomec, sexoc, matriculac, senhac, turmac)
    aluno.Cadastrar()
def cadastrar_professor(nome_c, sexo_c, matricula_c, senha_c):
    professor = Professor(nome_c, sexo_c, matricula_c, senha_c)
    professor.Cadastrar()