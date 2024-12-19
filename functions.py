class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}"


class Aluno(Pessoa):
    def __init__(self, matricula, nome, email):
        super().__init__(nome, email)
        self.matricula = matricula

    def __str__(self):
        return f"Matrícula: {self.matricula}, {super().__str__()}"


class Professor(Pessoa):
    def __init__(self, id_professor, nome, email):
        super().__init__(nome, email)
        self.id_professor = id_professor

    def __str__(self):
        return f"ID: {self.id_professor}, {super().__str__()}"


class Materia:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.professor = None  # Composição: matéria tem um professor

    def atribuir_professor(self, professor):
        self.professor = professor

    def __str__(self):
        professor_info = f"Professor: {self.professor.nome}" if self.professor else "Sem professor atribuído"
        return f"Código: {self.codigo}, Nome: {self.nome}, {professor_info}"


class Escola:
    def __init__(self):
        self.alunos = {}
        self.materias = {}
        self.professores = {}
        self.proxima_matricula = 250000000
        self.proximo_id_professor = 1000

    def cadastrar_aluno(self, nome, email):
        if any(aluno.nome == nome for aluno in self.alunos.values()):
            print("Erro: Nome já cadastrado")
            return

        aluno = Aluno(self.proxima_matricula, nome, email)
        self.alunos[self.proxima_matricula] = aluno
        print(f"Aluno cadastrado com sucesso! Matrícula: {self.proxima_matricula}")
        self.proxima_matricula += 1

    def remover_aluno(self, matricula):
        if matricula not in self.alunos:
            print("Erro: Matrícula não encontrada")
        else:
            removido = self.alunos.pop(matricula)
            print(f"Aluno {removido.nome} removido com sucesso!")

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in self.alunos.values():
                print(aluno)

    def cadastrar_materia(self, codigo, nome):
        if codigo in self.materias:
            print("Erro: Código de matéria já cadastrado")
            return

        if any(materia.nome == nome for materia in self.materias.values()):
            print("Erro: Matéria já cadastrada")
            return

        materia = Materia(codigo, nome)
        self.materias[codigo] = materia
        print("Matéria cadastrada com sucesso!")

    def remover_materia(self, codigo):
        if codigo not in self.materias:
            print("Erro: Código de matéria não encontrado")
        else:
            removida = self.materias.pop(codigo)
            print(f"Matéria {removida.nome} removida com sucesso!")

    def listar_materias(self):
        if not self.materias:
            print("Nenhuma matéria cadastrada.")
        else:
            for materia in self.materias.values():
                print(materia)

    def cadastrar_professor(self, nome, email):
        if any(professor.nome == nome for professor in self.professores.values()):
            print("Erro: Nome já cadastrado")
            return

        professor = Professor(self.proximo_id_professor, nome, email)
        self.professores[self.proximo_id_professor] = professor
        print(f"Professor cadastrado com sucesso! ID: {self.proximo_id_professor}")
        self.proximo_id_professor += 1

    def listar_professores(self):
        if not self.professores:
            print("Nenhum professor cadastrado.")
        else:
            for professor in self.professores.values():
                print(professor)

    def atribuir_professor_a_materia(self, codigo_materia, id_professor):
        if codigo_materia not in self.materias:
            print("Erro: Matéria não encontrada")
            return

        if id_professor not in self.professores:
            print("Erro: Professor não encontrado")
            return

        materia = self.materias[codigo_materia]
        professor = self.professores[id_professor]
        materia.atribuir_professor(professor)
        print(f"Professor {professor.nome} atribuído à matéria {materia.nome}")


def menu_opcoes(opcoes):
    print("----------Sistema de Gerenciamento------------")
    for idx, opcao in enumerate(opcoes, start=1):
        print(f"{idx} - {opcao}")
    print(f"{len(opcoes) + 1} - Sair")
    return input("--> ")
