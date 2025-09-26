# Condicionais - if, elif & else

# Exemplo 1
"""
Fala Jedi! Bora sair hoje?
Se não estiver chovendo vamos!
"""

esta_chovendo = False

if esta_chovendo == False:
    print("Bora! :) ")
else: 
    print("Não Posso Sair! :/ ")


# Exemplo 2
"""
Hey Jedi, pode me ajudar a carregar essas caixas usando a força?
Se eu estiver livre, sim. Mas caso não esteja peça ao Obi Wan para te ajudar
"""

estou_livre = False

if estou_livre == True:
    print("Irei te Ajudar! :) ")
else:
    print("Peça Ajuda ao Obi! :P ")

# Exemplo 3 
"""
Estou Atrasado. Posso Participar do Treino?
Se for sua primeira ou segunda vez que chega atrasado, sim. Mas Caso seja a terceira você não poderá.
"""

atrasos = int(input("Informe Sua Quantidade de Atrasos: "))
if atrasos >= 3:
    print("PÁ! Acesso Negado ksksks")
elif atrasos == 2:
    print("Falta 1 atraso para ser negado.")
elif atrasos == 1:
    print("Faltam 2 atrasos para ser negado.")
else:
    print("Pode Entrar! :) ")
    
