from classes import *
import os

def cadastrar_aluno(nomec, sexoc, matriculac, senhac, turmac):
    aluno = Aluno(nomec, sexoc, matriculac, senhac, turmac)
    aluno.Cadastrar()
def cadastrar_professor(nome_c, sexo_c, matricula_c, senha_c):
    professor = Professor(nome_c, sexo_c, matricula_c, senha_c)
    professor.Cadastrar()

def limpar_terminal():
    os.system('cls')

def login(matricula_login_aluno,senha_login_aluno, tipo_usuario):
    usuario  = Usuario(None, None, matricula_login_aluno, senha_login_aluno)
    usuario.Login(tipo_usuario)