"""
Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas. 
Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. 
Sua tarefa é criar um programa que realize essa operação. 
"""

equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 

tarefas = equipe_b.union(equipe_a)

print(f'Tarefas: {', '.join(tarefas)}')

excluir = input("qual tarefa você quer excluir: ").lower()

if excluir in tarefas:
    tarefas.remove(excluir)

print(f'Tarefas finais: {', '.join(tarefas)}')