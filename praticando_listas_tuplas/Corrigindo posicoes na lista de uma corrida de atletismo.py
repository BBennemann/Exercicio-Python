"""
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes.
Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?
"""

lista = ['Ana', 'Carlos', 'Pedro']

print(f"Lista desatualizada: {lista}")
nome_errado = input("Digite o nome incorreto: ")
nome_certo = input("Digite o nome correto: ")

if nome_errado in lista:
    posicao = lista.index(nome_errado)
    lista.remove(nome_errado)
    lista.insert(posicao, nome_certo)

    print(f"Lista atualizada: {lista}")
else:
    print("Nome não encontrado!")


