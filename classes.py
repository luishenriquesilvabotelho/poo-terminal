import sqlite3



class Usuario:
    def __init__(self,nome,sexo,matricula,senha):

        self.nome = nome
        self.sexo = sexo
        self.matricula = matricula
        self.senha = senha

    def Cadastrar(self, a, b):
        with sqlite3.connect("banco_de_dados.db") as banco:
            cursor = banco.cursor()
            if a == "Aluno":
                cursor.execute("INSERT INTO Aluno VALUES (?, ?, ?, ?, ?)", (
                    self.nome, self.matricula, self.senha, self.sexo, b))
                banco.commit()

            elif a == "Professor":
                cursor.execute("INSERT INTO Professor (nome, matricula, senha, sexo) VALUES (?, ?, ?, ?)",
                            (self.nome, self.matricula, self.senha, self.sexo))
                banco.commit()

    def Login(self, usuario):
        with sqlite3.connect("banco_de_dados.db") as banco:
            cursor = banco.cursor()
            if usuario == 'Aluno':
                cursor.execute(
                "SELECT * FROM Aluno WHERE (matricula == ? AND senha == ?)", (self.matricula, self.senha))
                verificador = cursor.fetchall()
                if len(verificador) > 0:
                    print("Login feito com sucesso!")
                    return True
                else:
                    print("Alguma coisa estava incorreta!")
                    return False
            elif usuario == 'Professor':
                cursor.execute(
                "SELECT * FROM Professor WHERE (matricula == ? AND senha == ?)", (self.matricula, self.senha))
                verificador = cursor.fetchall()
                if len(verificador) > 0:
                    print("Login feito com sucesso!")
                    return True
                else:
                    print("Alguma coisa estava incorreta!")
                    return False


class Aluno(Usuario):
    def __init__(self, nome, sexo, matricula, senha, turma):
        super().__init__(nome, sexo, matricula, senha)
        self.turma = turma

    def Cadastrar(self):
        super().Cadastrar("Aluno", self.turma)

    def ExibirAlunos(self):
        print('a')


class Professor(Usuario):
    def __init__(self, nome, sexo, matricula, senha):
        super().__init__(nome, sexo, matricula, senha)

    def Cadastrar(self):
        return super().Cadastrar("Professor", None)
    
    
    def EditarInscricoes(self):
        print("oi")



