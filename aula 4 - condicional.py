faturamento = 1000
custo = 1000
lucro = faturamento - custo

# if condiçao / comparação:
#   o que eu quero que aconteça se a condição for verdadeira 
# else:
#   o que eu quero que aconteça se a condição for falsa

if lucro > 0:
    print(f"Lucro de {lucro}")
elif lucro == 0: # == para comparação (igual em C)
    print(f"Estaca zero")
else:
    print(f"Prejuízo de {lucro}")

# operadores lógicos:
# e -> and
# ou -> or
# negação -> not