# Listas

precos = [20, 50, 100]

"""
. Pode-se Refererir a um Item Específico dentro de uma Lista, Basta apenas indicar no índice da mesma.
. Ex.:
    precos = [20, 50, 100]
               0   1   2 
"""

print(precos[1])


"""
. O índice Sempre é um valor numérico, mesmo se a lista se tratar de Strings
. Ex.:
    nomes = ["Brasil", "México", "Alemanha", "Canadá"]
                0          1          2          3
"""

nomes = ["Brasil", "México", "Alemanha", "Canadá"]
print(nomes[2])

# Encontrar o Índice Automaticamente

print(nomes.index("Canadá"))


# Manipular -> Add Novos Items (.append())

salarios = [2500, 5000, 7000]
salario_informado = float(input("Informe o Seu Salário: "))

salarios.append(salario_informado)

print(salarios)