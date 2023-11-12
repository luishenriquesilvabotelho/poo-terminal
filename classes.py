
import sqlite3
import random
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
        super().Cadastrar("Aluno", self.turma)



    def VerificarSenha(self, senha):
        return self.senha == senha
    # def EditarInscricoes(self, escolha_p_editar):
    #     with sqlite3.connect("banco_de_dados.db") as banco:
    #         cursor = banco.cursor()
    #         if escolha_p_editar == 1: # EDITAR NOME
    #             cursor.execute("UPDATE Aluno SET nome = ? WHERE matricula = ?", (self.nome, self.matricula))
    #         elif escolha_p_editar == 2: # EDITAR MATRÍCULA
    #             # A matrícula não deve ser editada, é um valor único.
    #             print("A matrícula não pode ser editada.")
    #         elif escolha_p_editar == 3: # EDITAR SENHA
    #             cursor.execute("UPDATE Aluno SET senha = ? WHERE matricula = ?", (self.senha, self.matricula))
    #         elif escolha_p_editar == 4: # EDITAR SEXO
    #             cursor.execute("UPDATE Aluno SET sexo = ? WHERE matricula = ?", (self.sexo, self.matricula))
    #         elif escolha_p_editar == 5: # EDITAR TURMA
    #             cursor.execute("UPDATE Aluno SET turma = ? WHERE matricula = ?", (self.turma, self.matricula))
    #         banco.commit()

        



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

def EditarInscricoes(self):
        print("Editando inscrições")


# class Chave:
#     def __init__(self, turmas):
#         self.turmas = turmas
#         self.chaveamento = []

#     def OrganizarTimes(self):
#         # Criar um dicionário para armazenar os times por turma
#         times_por_turma = {}
#         for turma in self.turmas:
#             times_por_turma[turma] = []

#         # Consultar o banco de dados para obter os alunos por turma
#         with sqlite3.connect("banco_de_dados.db") as banco:
#             cursor = banco.cursor()
#             cursor.execute("SELECT nome, turma FROM Aluno")
#             alunos = cursor.fetchall()
            
#             for aluno in alunos:
#                 nome, turma = aluno
#                 times_por_turma[turma].append(nome)

#         # Exibir os times organizados por turma
#         for turma, times in times_por_turma.items():
#             print(f"Turma: {turma}")
#             for time in times:
#                 print(f"  - {time}")
#             print()

#     def GerarChave(self):
#         # Embaralhar aleatoriamente as turmas para criar o chaveamento
#         random.shuffle(self.turmas)

#         # Criar as disputas em pares
#         for i in range(0, len(self.turmas), 2):
#             if i + 1 < len(self.turmas):
#                 disputa = (self.turmas[i], self.turmas[i + 1])
#                 self.chaveamento.append(disputa)

#     def ExibirChave(self):
#         # Exibir o chaveamento
#         for i, disputa in enumerate(self.chaveamento, start=1):
#             turma1, turma2 = disputa
#             print(f"Disputa {i}: {turma1} x {turma2}")

#Sem resultados tbm