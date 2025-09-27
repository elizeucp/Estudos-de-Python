# Projeto 3 - Medidor de Velocidade
"""
. Crie um Programa que receba do usuário um valor que represente a velocidade em uma via cuja velocidade máxima permitida é de 80 km/h.

. Com Base Nesse valor, o programa deve informar se o motorista levou uma multa Leve, Grave ou Gravíssima.

. Se a Velocidade estiver abaixo ou igual a 80 km/h, Exiba: "Não houve Multa!"
. Se Estiver Até 10 km/h acima, Exiba: "Levou Multa Leve!"
. Se Estiver entre 11 km/h e 20 km/h acima, Exiba: "Levou Multa Grave!"
. Se Estiver Acima de 20 km/h acima, Exiba: "Levou Multa Gravísima!"
"""

velocidade = int(input("Velocidade da Via: 80km/h | Informe Sua Velocidade Atual: "))

if velocidade <= 80:
    print("Não Houve Multa!")
elif velocidade-80 <= 10:
    print("Levou Multa Leve!")
elif velocidade-80 > 10 and velocidade-80 <= 20:
    print("Levou Multa Grave!")
else:
    print("Levou Multa Gravissima!")

