"""
Carlos precisa calcular o fatorial de cinco números diferentes simultaneamente. 
Como cálculos pesados podem demorar, ele quer garantir que todos sejam processados ao mesmo tempo, 
e os resultados exibidos assim que estiverem prontos.

Crie um programa que calcule o fatorial de cinco números diferentes de forma assíncrona, 
onde os cálculos devem ser realizados paralelamente e exiba os resultados conforme forem concluídos, 
em ordem de menor número para maior número.
"""

import asyncio

numeros = [5, 3, 7, 4, 6]

def fatorial(numero):
    x = 0

    if numero == 0 or numero == 1:
        return 1
    else:
        x += numero * fatorial(numero - 1)
        return x

async def calcular(numero):
    await asyncio.sleep(numero)
    print(fatorial(numero))

async def main():
    tarefas = [asyncio.create_task(calcular(n)) for n in numeros]
    await asyncio.gather(*tarefas)

asyncio.run(main())