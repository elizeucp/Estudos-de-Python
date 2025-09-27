# Projeto 2 - Chute o Número

"""
. Escreva um Programa que, ao iniciar, gere um valor Aleatório de 1 a 10 e permita que o Usuário Chute Números até acertar o valor gerado.

. O Programa deve Informar se o Chute foi Maior, Menor ou Igual o Valor Aleatório Gerado no Início. 
"""

import random

numero_aleatorio = random.randint(1,10)
chute = 0

print("O Número foi Gerado!")

while chute != numero_aleatorio:
    chute = int(input("Chute o Número: "))
    if (chute > numero_aleatorio):
        print(f"O Número {chute} é Maior que o Valor Gerado!")
    elif chute < numero_aleatorio:
        print(f"O Número {chute} é Menor que o Valor Gerado!")
print("Parabéns, Você Acertou!")
