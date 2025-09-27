# Fatorial de Um Numero

numero = int(input("Informe o Número: "))
fatorial = 1

for item in range(1, numero + 1):
    print(f"{fatorial} * {item}")
    fatorial = fatorial * item
    print(fatorial)
print(f"{numero}! = {fatorial}")