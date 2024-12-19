# arquivo: main.py

from functions import Escola, menu_opcoes

def main():
    escola = Escola()

    while True:
        opcao = menu_opcoes([
            "Cadastrar Aluno",
            "Listar Alunos",
            "Remover Aluno",
            "Cadastrar Professor",
            "Listar Professores",
            "Cadastrar Matéria",
            "Listar Matérias",
            "Atribuir Professor a Matéria",
            "Remover Matéria"
        ])

        if opcao == "1":
            nome = input("Nome do aluno: ")
            email = input("Email do aluno: ")
            escola.cadastrar_aluno(nome, email)
        elif opcao == "2":
            escola.listar_alunos()
        elif opcao == "3":
            matricula = int(input("Matrícula do aluno a ser removido: "))
            escola.remover_aluno(matricula)
        elif opcao == "4":
            nome = input("Nome do professor: ")
            email = input("Email do professor: ")
            escola.cadastrar_professor(nome, email)
        elif opcao == "5":
            escola.listar_professores()
        elif opcao == "6":
            codigo = input("Código da matéria: ")
            nome = input("Nome da matéria: ")
            escola.cadastrar_materia(codigo, nome)
        elif opcao == "7":
            escola.listar_materias()
        elif opcao == "8":
            codigo = input("Código da matéria: ")
            id_professor = int(input("ID do professor: "))
            escola.atribuir_professor_a_materia(codigo, id_professor)
        elif opcao == "9":
            codigo = input("Código da matéria a ser removida: ")
            escola.remover_materia(codigo)
        elif opcao == "10":
            print("Saindo do sistema... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
