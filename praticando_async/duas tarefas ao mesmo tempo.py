"""
Carlos é um engenheiro de software que precisa processar duas tarefas simultaneamente: 
uma que simula um download e outra que simula uma análise de dados. 
Ele quer que ambas as tarefas sejam iniciadas ao mesmo tempo, e que 
o programa exiba mensagens informando o início e o fim de cada uma.

Com base nesse cenário, crie um programa que inicie ambas as tarefas ao mesmo tempo, 
e exiba as mensagens quando cada uma for concluída. Dica: Utilize asyncio.gather() para rodar ambas em paralelo. 
"""

import asyncio

async def download():
    print("iniciando download")
    await asyncio.sleep(4)
    print("Download finalizado após 4 segundos")

async def analise():
    print("inciando analise de dados")
    await asyncio.sleep(2)
    print("Finalizando analise de dados após 2 segundos")

async def main():
    await asyncio.gather(download(), analise())

asyncio.run(main())