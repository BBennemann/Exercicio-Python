"""
Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.
"""

def menu():
    print("         Gerenciador de tarefas")
    print("-="*20)
    print("""1. Adicionar tarefa
2. Visualizar tarefas
3. Remover tarefa
4. Sair""")
    print("-=" * 20)
    escolha = input("Escolha uma opção: ")
    if escolha.isnumeric():
        escolha = int(escolha)
    return escolha

def funcoes():
    tarefas = []
    escolha = 0
    while escolha != 4:
        escolha = menu()
        match escolha:
            case 1:
                tarefa = input("Digite o nome da tarefa: ").strip()
                tarefas.append(tarefa)
                print("tarefa adicionada!")
            case 2:
                print("Tarefas: ")
                for x in tarefas:
                    print(f"-- {x}")
            case 3:
                print(tarefas)
                tarefa = input("Qual tarefa deseja remover? ")
                if tarefa in tarefas:
                    tarefas.remove(tarefa)
                    print("Tarefa removida!")
                else:
                    print("Por favor digite uma tarefa valida!")
            case 4:
                print("Adeus!")
            case _:
                escolha = 0
                print("Por favor escolha um número valido!")
        print("-=" * 20)

funcoes()