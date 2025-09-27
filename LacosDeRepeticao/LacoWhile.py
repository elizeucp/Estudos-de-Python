# Laços de Repetição (While)

# Estrutura Básica
"""
while Condição:
    # Código a ser Executado
"""


# Execute um Programa que Permita 3 Tentativas Antes de Fechar

tentativas = 0

while tentativas < 3:
    print(f"Tente novamente. | {tentativas}")
    tentativas += 1




# Quando Queremos que um Ação Aconteça Até que um Critério Seja Satisfeito.
# Só pode Logar se a Senha Estiver Correta.

senha = ""

while senha != "123456":
    senha = input("Digite sua Senha: ")
print("Usuário Logado!")




# Garantir que Algo Esteja Preenchido
# Só Deve Continuar caso o Usuário Informe Seu Nome

nome = ""

while nome == "":
    nome = input("Informe Seu Nome: ")
print(f"Seja Bem-Vindo {nome}!")




# Contadores Dentro de um While
# Ser Avisado as 17hrs do Por do Sol
# Contar de Hora em Hora até chegar as 17hrs
# ao chegar as 17hrs, exibir: "Hora do Por do Sol"

horario = 0

while horario <= 17:
    print(f"Horário Atual: {horario}")
    horario += 1
horario = 17
print(f"Hora do Por do Sol! | Horário Atual: {horario}")

