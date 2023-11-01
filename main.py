from funcoes import *
from classes import *
import os

def limpar_terminal():
    os.system('cls')


    
limpar_terminal()
print('Seja bem vindo ao nosso sistema\nEscolha umas das opções abaixo')

login_ou_cadastro = int(input('[1] - Login\n[2] - Cadastro\n'))
limpar_terminal()
while login_ou_cadastro != 1 and login_ou_cadastro != 2:
    limpar_terminal()
    print('Você digitou algo incorretamente')
    login_ou_cadastro = int(input('[1] - Login\n[2] - Cadastro\n'))
    
if login_ou_cadastro == 1: #LOGIN
    print('Você irá Logar como?')
    aluno_ou_prof = int(input('[1] - Aluno\n[2] - Professor\n'))
    
    while aluno_ou_prof != 1 and aluno_ou_prof != 2:
        limpar_terminal()
        print('Você digitou algo incorretamente')
        aluno_ou_prof = int(input('[1] - Aluno\n[2] - Professor'))
        
    if aluno_ou_prof == 1: # LOGIN -> ALUNO
        print('Aluno')
        
    if aluno_ou_prof == 2: # LOGIN -> PROFESSOR
        print('Prof')
    
elif login_ou_cadastro == 2: #CADASTRO
    aluno_ou_prof = int(input('[1] - Aluno\n[2] - Professor'))
    if aluno_ou_prof == 1:
        limpar_terminal()
        print("Bem vindo(a)")
        nome_aluno = input("Digite seu nome: ")
        sexo_aluno = input("Digite seu sexo: ")
        matricula_aluno = int(input("Digite sua matrícula: "))
        senha_aluno = input("Digite sua senha: ")
        turma_aluno = input("Digite sua turma: ")
        aluno_cadastrado = Aluno(nome_aluno,sexo_aluno,matricula_aluno,senha_aluno,turma_aluno)
        cadastrar_aluno(nome_aluno, sexo_aluno, matricula_aluno, senha_aluno, turma_aluno)
    else:
        limpar_terminal()
        print("Bem vindo(a)")
        nome_prof = input("Digite seu nome: ")
        sexo_prof = input("Digite seu sexo: ")
        matricula_prof = int(input("Digite sua matrícula: "))
        senha_prof = input("Digite sua senha: ")
        professor_cadastrado = Professor(nome_prof, sexo_prof, matricula_prof, senha_prof)
        cadastrar_professor(nome_prof, sexo_prof, matricula_prof, senha_prof)

    