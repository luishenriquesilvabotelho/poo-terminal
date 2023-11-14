from funcoes import *
from classes import *
import os

try:
    limpar_terminal()
    print('Seja bem-vindo ao nosso sistema\nEscolha uma das opções abaixo')

    login_ou_cadastro = int(input('[1] - Login\n[2] - Cadastro\n'))
    limpar_terminal()
    while login_ou_cadastro != 1 and login_ou_cadastro != 2:
        limpar_terminal()
        print('Você digitou algo incorretamente')
        login_ou_cadastro = int(input('[1] - Login\n[2] - Cadastro\n'))

    if login_ou_cadastro == 1:  # LOGIN
        print('Você irá Logar como?')
        aluno_ou_prof = int(input('[1] - Aluno\n[2] - Professor\n'))

        while aluno_ou_prof != 1 and aluno_ou_prof != 2:
            limpar_terminal()
            print('Você digitou algo incorretamente')
            aluno_ou_prof = int(input('[1] - Aluno\n[2] - Professor'))

        if aluno_ou_prof == 1:  # LOGIN -> ALUNO
            limpar_terminal()
            print('Insira seus dados')
            input_mat_login_aluno = int(input('Matrícula: '))
            input_senha_login_aluno = input('Senha: ')
            usuario = Usuario(None, None, input_mat_login_aluno, input_senha_login_aluno)
            if usuario.Login(aluno_ou_prof):
                while True:  # Adicione um loop para o menu do aluno
                    limpar_terminal()
                    print('========Menu do Aluno===========')
                    print('[1] - Editar seus dados\n[2] - Esqueceu sua senha?\n[0] - Sair')
                    menu_aluno_escolha = int(input('Escolha uma das opções acima: '))

                    if menu_aluno_escolha == 1:
                        try:
                            aluno_verifica_mat = int(input('MAT'))
                            aluno_verifica_senha = input('senha')
                            aluno_mudar = Aluno(None, None, aluno_verifica_mat, aluno_verifica_senha, None)
                            aluno_mudar.VerificarSenha()
                        except ValueError:
                            print("Por favor, insira um valor numérico para a matrícula.")
                    elif menu_aluno_escolha == 2:
                        pass
                    elif menu_aluno_escolha == 0:
                        quit()
                    else:
                        print("Opção inválida. Tente novamente.")

        if aluno_ou_prof == 2:  # LOGIN -> PROFESSOR
            limpar_terminal()
            print('Insira seus dados')
            input_mat_login_prof = int(input('Matrícula: '))
            input_senha_login_prof = input('Senha: ')
            usuario2 = Professor(None, None, input_mat_login_prof, input_senha_login_prof)
            if usuario2.Login(aluno_ou_prof):
                limpar_terminal()
                print('========Menu do Aluno===========')
                print("[1]-Ver Alunos escritos\n[2] - Organizar Chave")
                escolha_prof = int(input("Escolha uma das opções acima: "))
                if escolha_prof == 1:
                    print("Alunos cadastrados no sistema ")
                    usuario2.ExibirAlunos()
                elif escolha_prof == 2:
                    limpar_terminal()
                    print('======== Interagir com Chave =========')
                    try:
                        # Consultar o banco de dados para obter as turmas cadastradas
                        with sqlite3.connect("banco_de_dados.db") as banco:
                            cursor = banco.cursor()
                            cursor.execute("SELECT DISTINCT turma FROM Aluno")
                            turmas_cadastradas = [turma[0] for turma in cursor.fetchall()]

                        # Criar uma instância de Chave com as turmas cadastradas
                        chave_interacao = Chave(turmas_cadastradas)

                        # Opções para interagir com a Chave
                        while True:
                            print('[1] - Organizar Times')
                            print('[2] - Gerar Chave')
                            print('[3] - Exibir Chave')
                            print('[0] - Sair')

                            opcao_chave = int(input('Escolha uma opção: '))

                            if opcao_chave == 1:
                                limpar_terminal()
                                print('Organizando Times:')
                                chave_interacao.OrganizarTimes()

                            elif opcao_chave == 2:
                                limpar_terminal()
                                print('Gerando Chave:')
                                chave_interacao.GerarChave()
                                print('Chave gerada com sucesso!')

                            elif opcao_chave == 3:
                                limpar_terminal()
                                print('Exibindo Chave:')
                                chave_interacao.ExibirChave()

                            elif opcao_chave == 0:
                                break

                            else:
                                limpar_terminal()
                                print('Opção inválida. Tente novamente.')
                    except sqlite3.Error as e:
                        print(f"Erro ao interagir com a Chave: {e}")
            else:
                quit()

    elif login_ou_cadastro == 2:  # CADASTRO
        aluno_ou_prof = int(input('[1] - Aluno\n[2] - Professor'))
        if aluno_ou_prof == 1:
            limpar_terminal()
            print("Bem-vindo(a)")
            nome_aluno = input("Digite seu nome: ")
            sexo_aluno = input("Digite seu sexo: ")
            matricula_aluno = int(input("Digite sua matrícula: "))
            senha_aluno = input("Digite sua senha: ")

            # Dicionário de turmas
            turmas = {
                1: '1 INFO A',
                2: '1 INFO B',
                3: '1 ELET A',
                4: '1 ELET B',
                5: '1 EDIF A',
                6: '1 EDIF B',
                7: '1 QUIM A',
                8: '1 QUIM B',
                9: '2 INFO M',
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
            print("Turmas disponíveis:")
            for key, value in turmas.items():
                print(f"{key} - {value}")

            num_turma_aluno = int(input("Escolha o número da turma desejada: "))
            if num_turma_aluno in turmas:
                turma_aluno = turmas[num_turma_aluno]
                aluno = Aluno(nome_aluno, sexo_aluno, matricula_aluno, senha_aluno, turma_aluno)
                aluno.Cadastrar()
            else:
                print("Turma não encontrada!")

        else:
            limpar_terminal()
            print("Bem-vindo(a)")
            nome_prof = input("Digite seu nome: ")
            sexo_prof = input("Digite seu sexo: ")
            matricula_prof = int(input("Digite sua matrícula: "))
            senha_prof = input("Digite sua senha: ")
            professor = Professor(nome_prof, sexo_prof, matricula_prof, senha_prof)
            professor.Cadastrar()

except ValueError as ve:
    print(f"Erro de valor: {ve}")
except sqlite3.Error as se:
    print(f"Erro no SQLite: {se}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
