import sqlite3



class Usuario:
    def __init__(self,nome,sexo,matricula,senha):

        self.nome = nome
        self.sexo = sexo
        self.matricula = matricula
        self.senha = senha

    def Cadastrar(self, usuario, turma):
        with sqlite3.connect("banco_de_dados.db") as banco:
            cursor = banco.cursor()
            if usuario == "Aluno":
                cursor.execute("INSERT INTO Aluno VALUES (?, ?, ?, ?, ?)", (
                    self.nome, self.matricula, self.senha, self.sexo, turma))
                banco.commit()

            elif usuario == "Professor":
                cursor.execute("INSERT INTO Professor (nome, matricula, senha, sexo) VALUES (?, ?, ?, ?)",
                            (self.nome, self.matricula, self.senha, self.sexo))
                banco.commit()

    def Login(self, usuario):
        with sqlite3.connect("banco_de_dados.db") as banco:
            cursor = banco.cursor()
            if usuario == 1:
                cursor.execute(
                "SELECT * FROM Aluno WHERE (matricula == ? AND senha == ?)", (self.matricula, self.senha))
                verificador = cursor.fetchall()
                if len(verificador) > 0:
                    print("Aluno Logado com sucessp")
                    return True
                else:
                    print("Alguma coisa estava incorreta!")
                    return False
            elif usuario == 'Professor':
                cursor.execute(
                "SELECT * FROM Professor WHERE (matricula == ? AND senha == ?)", (self.matricula, self.senha))
                verificador = cursor.fetchall()
                if len(verificador) > 0:
                    print("Prof Logado com sucessor")
                    return True
                else:
                    print("Alguma coisa estava incorreta!")
                    return False


class Aluno(Usuario):
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
    def __init__(self, nome, sexo, matricula, senha, num_turma):
        super().__init__(nome, sexo, matricula, senha)
        self.num_turma = num_turma

    def Cadastrar(self):
        turma = Aluno.turmas.get(self.num_turma,f'Turma {self.num_turma} não encontrada')
        super().Cadastrar("Aluno", self.num_turma)

    def ExibirAlunos(self):
        print('a')


class Professor(Usuario):
    def __init__(self, nome, sexo, matricula, senha):
        super().__init__(nome, sexo, matricula, senha)

    def Cadastrar(self):
        return super().Cadastrar("Professor", None)
    
    
    def EditarInscricoes(self):
        print("oi")



