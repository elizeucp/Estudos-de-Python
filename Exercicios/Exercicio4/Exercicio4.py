# Exercício 4 (Laço While)
'''
Crie um Gerenciador de Login Simples, com no máximo 3 Tentativas
(Teremos Apenas um Único Usuário e Senha Permitido)

Usuário: Elizeu
Senha: SenhaForte

Após 3 Tentativas, Se o Usuário Estiver Errado, Exibir: "Aguarde 30min para Tentar Novamente!"
Se o Usuário Acertar o Usuário e Senha Antes Disso, Exibir: "Login Feito com Sucesso!"
'''

usuario = ""
senha = ""
tentativas = 0

while (usuario != "Elizeu" and senha != "SenhaForte") and tentativas < 3:
    usuario = input("Informe Seu Usuário: ")
    senha = input("Informe Sua Senha: ")
    tentativas += 1

if (usuario != "Elizeu" and senha != "SenhaForte"):
    print("Aguarde 30min para Tentar Novamente!")
else:
    print("Login Feito com Sucesso!")