# Exercício 3 (Laço For)
'''
Faça um Sistema que Informe se uma Senha é Válida ou Não.
Para uma Senha ser Válida ela precisa ter pelomenos 6 caracteres.
'''

"""
len(variavel) -> Quantidade de Carácteres.
"""

# Resposta

senhas = ["abc", "teste123", "senha1", "123", "samuel123"]

for senha in senhas:
    if len(senha) >= 6:
        print(f"A Senha {senha} é válida!")
    else:
        print(f"A Senha {senha} NÃO é válida!")