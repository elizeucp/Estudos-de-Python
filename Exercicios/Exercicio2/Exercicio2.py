# Exercício 2 (Condicionais)
'''
Crie um Programa que Receba Dois Valores e Imprima o Maior Valor entre eles.
'''

# Resposta
primeiro_valor = int(input("Informe o Primeiro Valor:"))
segundo_valor = int(input("Informe o Segundo Valor:"))

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor} é maior que {segundo_valor}. | {primeiro_valor} > {segundo_valor}")
else:
    print(f"{segundo_valor} é maior que {primeiro_valor}. | {segundo_valor} > {primeiro_valor}")
