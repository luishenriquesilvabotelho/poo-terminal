
import sqlite3
import random

#Turma: 2 INFO V
# Aluno: Luis Henrique, Marcos Aurelio, Daniel Guimarães E Danielly Vitória
class Usuario:
    def __init__(self, nome, sexo, matricula, senha):
        self.nome = nome
        self.sexo = sexo
        self.matricula = matricula
        self.senha = senha

    def Cadastrar(self, usuario, turma=None):
        with sqlite3.connect("banco_de_dados.db") as banco:
            cursor = banco.cursor()
            if usuario == "Aluno":
                cursor.execute("INSERT INTO Aluno VALUES (?, ?, ?, ?, ?)", (
                    self.nome, self.matricula, self.senha, self.sexo, turma))
                banco.commit()
                print("Aluno cadastrado com sucesso")

            elif usuario == "Professor":
                cursor.execute("INSERT INTO Professor (nome, matricula, senha, sexo) VALUES (?, ?, ?, ?)",
                            (self.nome, self.matricula, self.senha, self.sexo))
                banco.commit()
                print("Professor cadastrado com sucesso")
            else:
                raise ValueError("Tipo de usuário invalido ao cadastrar")

    def Login(self, usuario):
        with sqlite3.connect("banco_de_dados.db") as banco:
            cursor = banco.cursor()
            if usuario == 1:
                cursor.execute("SELECT * FROM Aluno WHERE matricula = ? AND senha = ?",
                            (self.matricula, self.senha))
                verificador = cursor.fetchall()
                if len(verificador) > 0:
                    print("Aluno logado com sucesso")
                    return True
                else:
                    print("Matrícula ou senha incorretas!")
                    return False
            elif usuario == 2:
                cursor.execute("SELECT * FROM Professor WHERE matricula = ? AND senha = ?",
                                (self.matricula, self.senha))
                verificador2 = cursor.fetchall()
                if len(verificador2) > 0:
                    print("Professor logado com sucesso!")
                    return True
                else:
                    print("Matrícula ou senha incorretas!")
                    return False
                


class Aluno(Usuario):

    def __init__(self, nome, sexo, matricula, senha, turma):
        super().__init__(nome, sexo, matricula, senha)
        self.turma = turma

    def Cadastrar(self):
        try:
            super().Cadastrar("Aluno", self.turma)
        except Exception as e:
            print(f"Ocorreu um erro no seu cadastro: {e}")

    def ObterDisputasTurma(self):
        try:
            with sqlite3.connect("banco_de_dados.db") as banco:
                cursor = banco.cursor()
                cursor.execute("SELECT * FROM Disputa WHERE turma1 = ? OR turma2 = ?", (self.turma, self.turma))
                disputas_turma = cursor.fetchall()
                return disputas_turma
        except Exception as e:
            print(f"Ocorreu um erro enquanto buscava as disputas de sua turma {e}")
            return []

    def VerificarSenha(self):
        try:
            with sqlite3.connect("banco_de_dados.db") as banco:
                cursor = banco.cursor()
                cursor.execute("SELECT * FROM Aluno WHERE matricula = ? AND senha = ?",
                            (self.matricula, self.senha))
                verificador = cursor.fetchall()
                if len(verificador) > 0:
                    print('MENU DE EDIÇÃO')
                    print('[1]-Nome\n[2]- Matricula\n[3]-Senha\n[4]-Sexo\n[5]-Turma\n')
                    escolha_editar = int(input(':'))

                    if escolha_editar == 1:
                        novo_nome = input('Novo nome: ')
                        cursor.execute("UPDATE Aluno SET nome = ? WHERE matricula = ?", (novo_nome, self.matricula))

                    elif escolha_editar == 2:
                        nova_matricula = int(input('Nova matrícula: '))
                        cursor.execute("UPDATE Aluno SET matricula = ? WHERE matricula = ?", (nova_matricula, self.matricula))

                    elif escolha_editar == 3:
                        nova_senha = input('Nova senha: ')
                        cursor.execute("UPDATE Aluno SET senha = ? WHERE matricula = ?", (nova_senha, self.matricula))

                    elif escolha_editar == 4:
                        novo_sexo = input('Novo sexo: ')
                        cursor.execute("UPDATE Aluno SET sexo = ? WHERE matricula = ?", (novo_sexo, self.matricula))

                    elif escolha_editar == 5:
                        nova_turma = input('Nova turma: ')
                        cursor.execute("UPDATE Aluno SET turma = ? WHERE matricula = ?", (nova_turma, self.matricula))

                    banco.commit()
                    print('Dados atualizados com sucesso!')
                    return True

                else:
                    print("Matrícula ou senha incorretas!")
                    return False
        except Exception as e:
            print(f"Ocorreu um erro na hora de verificar sua senha: {e}")
            return False

class Professor(Usuario):
    def __init__(self, nome, sexo, matricula, senha):
        super().__init__(nome, sexo, matricula, senha)

    def Cadastrar(self):
        return super().Cadastrar("Professor")
    
    def ExibirAlunos(self):
        banco = sqlite3.connect("banco_de_dados.db")
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT nome, turma, sexo, matricula FROM Aluno")
        except sqlite3.OperationalError:
            print("Erro: Tabela Alunos não encontrada.")
            return
        mostrar_alunos = cursor.fetchall()
        alunos_por_turmas = {
        }
        if mostrar_alunos:
            for alunos in mostrar_alunos:
                nome = alunos[0]
                turma = alunos[1]
                sexo = alunos[2]
                matricula = alunos[3]
                if turma in alunos_por_turmas:
                    alunos_por_turmas[turma].append({
                        "Nome": nome,
                        "Sexo": sexo,
                        "Matricula": matricula
                    })
                else:
                    alunos_por_turmas[turma]= [{
                        "Nome": nome,
                        "Sexo": sexo,
                        "Matricula": matricula
                    }]
            for turma, alunos in alunos_por_turmas.items():
                print(f"Turma: {turma}")
                for aluno in alunos:
                    print(f"Nome: {aluno['Nome']}")
                    print(f"Sexo: {aluno['Sexo']}")
                    print(f"Matricula: {aluno['Matricula']}")
                    print()
                
        else:
            print(f"Nenhuma aluno encontrado na turma {turma}")
        banco.close()

class ChaveError(Exception):
    pass

class Chave:
    def __init__(self, turmas):
        self.turmas = turmas
        self.chaveamento = []

    def OrganizarTimes(self):
        try:
            times_por_turma = {}
            for turma in self.turmas:
                times_por_turma[turma] = []
    
            with sqlite3.connect("banco_de_dados.db") as banco:
                cursor = banco.cursor()
                cursor.execute("SELECT nome, turma FROM Aluno")
                alunos = cursor.fetchall()

                for aluno in alunos:
                    nome, turma = aluno
                    times_por_turma[turma].append(nome)
    
            for turma, times in times_por_turma.items():
                print(f"Turma: {turma}")
                for time in times:
                    print(f"  - {time}")
                print()
        except sqlite3.Error as e:
            raise ChaveError(f"Erro ao acessar o banco de dados: {e}")
        except Exception as e:
            raise ChaveError(f"Ocorreu um erro inesperado ao organizar times: {e}")

    def GerarChave(self, times_por_disputa=2):
        
        try:
            if not self.turmas:
                raise ChaveError("Não há turmas para gerar chaveamento.")
            
            self.LimparChaveamento()

            random.shuffle(self.turmas)
            
            for i in range(0, len(self.turmas), times_por_disputa):
                disputa = tuple(self.turmas[i:i+times_por_disputa])
                self.chaveamento.append(disputa)
                self.inserir_disputa_no_banco(disputa)
        except IndexError as e:
            raise ChaveError(f"Erro ao gerar chave: {e}")
        except ChaveError as e:
            raise e
        except Exception as e:
            raise ChaveError(f"Ocorreu um erro inesperado ao gerar chave: {e}")

    def LimparChaveamento(self):
        self.chaveamento = []

    def inserir_disputa_no_banco(self, disputa):
        try:
            with sqlite3.connect("banco_de_dados.db") as banco:
                cursor = banco.cursor()
                cursor.execute('''
                    INSERT INTO Disputa (turma1, turma2) VALUES (?, ?)
                ''', disputa)
                banco.commit()
        except sqlite3.Error as e:
            raise ChaveError(f"Erro ao inserir disputa no banco de dados: {e}")
        except Exception as e:
            raise ChaveError(f"Ocorreu um erro inesperado ao inserir disputa no banco de dados: {e}")

    def ExibirChave(self):
        try:
            if not self.chaveamento:
                print("Nenhum chaveamento disponível.")
                return

            for i, disputa in enumerate(self.chaveamento, start=1):
                print(f"Disputa {i}: {' x '.join(disputa)}")
                
            self.LimparChaveamento
        except ChaveError as e:
            raise e
        except Exception as e:
            raise ChaveError(f"Ocorreu um erro inesperado ao exibir chave: {e}")




class Partida:
    def __init__(self, chaveamento):
        self.chaveamento = chaveamento
        self.horario = {}

    def obter_horario_partida(self):
        for i, disputa in enumerate(self.chaveamento, start=1):
            try:
                horario = input(f"Digite o horário da partida {i} entre {disputa[0]} x {disputa[1]} (por exemplo, 15:00)\nR: ")
                self.horario[i] = horario
            except Exception as e:
                print(f"Erro ao obter horário: {e}")

    def exibir_partida(self):
        for i, disputa in enumerate(self.chaveamento, start=1):
            turma1, turma2 = disputa
            print(f"Disputa {i}: {turma1} x {turma2}")
            if i in self.horario:
                print(f"Horário da Partida: {self.horario[i]}")
            else:
                print("Horário da Partida: Não definido")
            print("Times")
            for time in self.chaveamento:
                print(f" - {time[0]} vs {time[1]}")

class Boletim:
    def __init__(self, Horario, Local):
        self.Horario = Horario
        self.Local = Local

    def ExibirBoletim(self):
        print("===BOLETIM===")
        print(f"Horario: {self.Horario}")
        print(f"Local: {self.Local}")
        print(6 * "==")

    def EditarBoletim(self):
        print("====EDITAR BOLETIM====")
        print("1. Editar Horário")
        print("2. Editar Local")
        try:
            opcao = int(input("Escolha alguma opção?\nR: "))
            with sqlite3.connect("banco_de_dados.db") as banco:
                cursor = banco.cursor()
                if opcao == 1:
                    novo_horario = input("Novo horário: ")
                    self.Horario = novo_horario
                    cursor.execute("UPDATE Boletim SET Horario = ? WHERE Local = ?", (novo_horario, self.Local))
                elif opcao == 2:
                    novo_local = input("Novo Local: ")
                    self.Local = novo_local
                    cursor.execute("UPDATE Boletim SET Local = ? WHERE Local = ?", (novo_local, self.Local))
                else:
                    print("Opção inválida.")
                banco.commit()
                print("Boletim editado com sucesso")
        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except sqlite3.Error as se:
            print(f"Erro no SQLite: {se}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
