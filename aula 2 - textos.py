faturamento = 1000
custo = 600
lucro = faturamento - custo

# texto = "O lucro foi de " + str(lucro) + " e o faturamento foi de " + str(faturamento)
# IMPORTANTE: só pode concatenar (juntar) texto com texto, por isso coloquei str(lucro) e str(faturamento).
# str() para poder transformar int em string.

texto = f"O lucro foi de R${lucro} e o faturamento foi de R${faturamento}" 
# f para formatar a string (exibir o valor contido na variável).
print(texto)

email = " RENAN_DEV@gmail.com "

# Como editar a variável email?
email = email.lower() # colocar em letra minúscula
email = email.strip() # ajustar espaços vazios

# Como exibir o email em letra minúscula?
print(email.lower())

# Como exibir o email com os espaços vazios ajustados?
print(email.strip())

# tamanho:
print(len(email)) # exibir quantos caracteres tem na string

# posição:
posicao = email.find("@") # encontra a posição (índice) do caractere @
print(posicao)

posicao_dois = email.find("n")
print(posicao_dois)

# pedaços do texto:
print(email[9:11]) # posição inicial é incluída e a posição final não é incluída! ou seja, no exemplo acima ele pega o 9 e 10.
print(email[9:]) # nesse caso, ele pega do 9 em diante (até o final da string)

servidor = email[posicao:] # pega o @ e tudo que vier depois dele
print(servidor)

servidor_dois = email[posicao + int(1):]
print(servidor_dois)

antes_servidor = email[:posicao] # pega tudo que vier antes do @ (@ não é incluído)
print(antes_servidor)

# trocar um pedaço do texto:
# exemplo: quero trocar 'gmail.com' por 'yahoo.com.br'
novo_email = email.replace("gmail.com", "yahoo.com.br")
print(novo_email)


# deixar a primeira letra da primeira palavra maiúscula:
nome = "renan morais"
nome = nome.capitalize()
print(nome)

# deixar a primeira letra de todas as palavras maiúscula:
nome = nome.title()
print(nome)

# deixar todas as letras maiúsculas:
nome = nome.upper()
print(nome)

# formatação numérica:
faturamento = 1_000_000
custo = 600

lucro = faturamento - custo
margem = (lucro / faturamento)

texto = f"O lucro foi de R${lucro:,.2f} e o faturamento foi de R${faturamento:,.2f}" # :, para exibir com separador de milhar
print(texto)                                                                         # .2f para exibir com duas casas decimais
texto_dois = f"A margem foi de R${margem:.1%}"
print(texto_dois)