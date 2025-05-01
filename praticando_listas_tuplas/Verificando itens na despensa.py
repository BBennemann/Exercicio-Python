"""
Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.

Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa.
Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.
"""

despensa = ["feijão", "arroz", "macarrão", "frango"]

while True:
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Digite 0 para sair!")
    item = input("Digite o item que você quer verificar: ").strip().lower()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    if item in despensa:
        print(f"O item {item} já foi comprado tente outro!")
    elif item == "0":
        break
    else:
        print(f"O item {item} precisa ser comprado!")

