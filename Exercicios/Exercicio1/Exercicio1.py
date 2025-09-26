# Exercício 1
'''
Escreva um Programa que retorne o Valor Hora de um Funcionário com base no seu Salário Mensal e Horas Trabalhadas por Mês. 
'''

# Resposta
salario_mensal = input("Informe o seu Salário Mensal: ")

horas_trabalhadas_mes = input("Informe as Horas Trabalhadas por Mês: ")

valor_hora = float(salario_mensal) / int(horas_trabalhadas_mes)

print(f"O Seu Valor Hora é de: {valor_hora:.2f} R$")


# Inserção de Variaveis em um Print
"""
. Como funciona o f-string?
Basta colocar um f antes das aspas da string. Dentro da string, você usa chaves {} para indicar onde deseja inserir o valor de uma variável ou o resultado de uma expressão.

. Exemplos básicos

nome = "Elizeu"
idade = 18

print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Saída: Meu nome é Elizeu e eu tenho 18 anos.

===========================================================

a = 5
b = 3
print(f"O resultado de {a} + {b} é {a + b}")

# Saída: O resultado de 5 + 3 é 8

===========================================================

valor = 2.34567
print(f"O valor formatado é {valor:.2f}")

# Saída: O valor formatado é 2.35
"""

