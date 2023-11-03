import sqlite3 as sql

from funcoes import *

limpar_terminal()
print('=' * 20)
print('1- Editar inscrições dos alunos\n2- Adicionar Horários\n3- Adicionar Turma')
print('=' * 20)
escolha = int(input(':'))

if escolha == 1:
    print('Você deseja consultar qual turma?')
    turmas = {
        1: '1 INFO A',
        2: '1 INFO B',
        3: '1 ELET A',
        4: '1 ELET B',
        5: '1 EDIF A',
        6: '1 EDIF B',
        7: '1 QUIM A',
        8: '1 QUIM B',
        9: ' 2 INFO M',
        10: '2 INFO V',
        11: '2 ELET M',
        12: '2 ELET V',
        13: '2 EDIF M',
        14: '2 EDIF V',
        15: '2 QUIM M',
        16: '2 QUIM V',
        17: '3 INFO M',
        18: '3 INFO V',
        19: '3 ELET M',
        20: '3 ELET V',
        21: '3 EDIF M',
        22: '3 EDIF V',
        23: '3 QUIM M',
        24: '3 QUIM V',
    }

    escolha_turma = int(input('Escolha a turma pelo índice: '))

    if escolha_turma in turmas:
        turma_escolhida = turmas[escolha_turma]
        print(f'Você escolheu a turma: {turma_escolhida}')
        with sqlite3.connect("banco_de_dados.db") as banco:
            cursor = banco.cursor()
            cursor.execute("SELECT nome, matricula FROM Aluno WHERE turma = ?", (turma_escolhida,))
            alunos = cursor.fetchall()
            if alunos:
                print(f'Alunos da turma {turma_escolhida}:')
                for aluno in alunos:
                    nome_aluno, matricula_aluno = aluno
                    print(f'Nome: {nome_aluno}, Matrícula: {matricula_aluno}')
            else:
                print(f'Nenhum aluno encontrado na turma {turma_escolhida}.')
    else:
        print('Índice de turma inválido.')


