
import sqlite3

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

    def Login(self, usuario):
        with sqlite3.connect("banco_de_dados.db") as banco:
            cursor = banco.cursor()
            if usuario == "Aluno":
                cursor.execute("SELECT * FROM Aluno WHERE matricula = ? AND senha = ?",
                               (self.matricula, self.senha))
                verificador = cursor.fetchall()
                if len(verificador) > 0:
                    print("Aluno logado com sucesso")
                    return True
                else:
                    print("Matrícula ou senha incorretas!")
                    return False
            elif usuario == "Professor":
                cursor.execute("SELECT * FROM Professor WHERE matricula = ? AND senha = ?",
                               (self.matricula, self.senha))
                verificador = cursor.fetchall()
                if len(verificador) > 0:
                    print("Professor logado com sucesso")
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

    def ExibirAlunos(self):
        print('Exibindo alunos')



class Professor(Usuario):
    def __init__(self, nome, sexo, matricula, senha):
        super().__init__(nome, sexo, matricula, senha)

    def Cadastrar(self):
        return super().Cadastrar("Professor")

    def EditarInscricoes(self):
        print("Editando inscrições")

