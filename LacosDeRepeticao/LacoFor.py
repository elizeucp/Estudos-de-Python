# Laços de Repetição (FOR)

# Estrutura Básica

"""
for Item in Coleção:
    # Comandos
"""

for item in range(3):
    print(item)



# Características
"""
. O range() nunca inclui o último valor, uma vez que inicia a partir do 0.
. Pode-se Indicar de onde o range() irá partir, basta colocar dentro de seu 1º parâmetro. Ex.: for item in range(1, 11): # Executaria do 1 até o 10.
. Pode-se Indicar o Passo que esse range() irá seguir, basta colocar em seu 3º parâmetro. Ex.: for item in range(1, 11, 2): # Executaria: 1, 3, 5, 7, 9.
"""

for item in range(2,11,2):
    print(item)



# Lista de Nomes
"""
. Pode-se usar um Array como Coleção para um Laço For.
"""
nomes = ["Samuel", "Heitor", "André", "Elizeu"]

for nome in nomes:
    print(nome)

"""
. Pode-se Misturar Diferentes Tipos de Dados Dentro da Lista.
"""

dados = ["Elizeu", 1, True, 17.7]

for dado in dados:
    print(dado)

"""
. Pode-se Usar Condicionais. Ex.: Exiba Somente os Maiores de Idade.
"""

idades = [15, 20, 19, 18, 40, 4, 1]

for idade in idades:
    if idade >= 18:
        print(f"{idade} anos é Maior de Idade. ")
    else: 
        print(f"{idade} anos é Menor de Idade. ")
