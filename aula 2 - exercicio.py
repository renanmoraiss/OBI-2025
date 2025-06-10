nome = "renan morais"
email = "emailfalsodorenan@gmail.com"

# 1. Descubra o servidor do email:
posicao_arroba_email = email.find("@")
servidor_email = posicao_arroba_email + int(1)
print(f"servidor do email: {email[servidor_email:]}")

# 2. Descubra o 1º nome do usuário:
posicao_primeiro_espaco = nome.find(" ")
primeiro_nome = (nome[:posicao_primeiro_espaco])
print(f"1º nome do usuário: {primeiro_nome}")

# 3. Deixar a primeira letra do 1º nome do usuário maiúscula:
primeiro_nome = primeiro_nome.capitalize()

# 4. Criar uma mensagem personalizada dizendo "Usuário 1º nome foi cadastrado com sucesso no email tal":
mensagem_personalizada = f"{primeiro_nome} foi cadastrado com sucesso no email: {email}!"
print(mensagem_personalizada)