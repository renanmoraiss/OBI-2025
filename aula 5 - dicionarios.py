lista_produtos = ["ipad", "iphone", "airpod"]
lista_precos = [7000, 5000, 2000]

# dicionário com 3 itens:
dic_produtos = {"ipad": 7000, "iphone": 5000, "airpod":2000}

# pegar o valor de um item:
print(dic_produtos["ipad"])

dic_vendas = {"lira": [1000, 500, 1500], "rodolfo": [500, 400, 500]}
print(dic_vendas["lira"])

# editar um item:
dic_produtos["iphone"] *= 1.1
print(dic_produtos)

# adicionar um item:
dic_produtos["macbook"] = 12000
print(dic_produtos)

# remover um item:
item_removido = dic_produtos.pop("macbook")
print(dic_produtos)
print(item_removido)

# verificar se existe um item no dicionário:
print("iphone" in dic_produtos) # True se encontrar e False se não encontrar.
print("iphone" in dic_produtos.keys()) # keys = chaves (no caso acima é ipad, iphone e airpod)
print(2000 in dic_produtos.values()) # values = valores (no caso acima é 7000, 5000 e 2000)


# criar uma lista só dos nomes a partir do dicionário:
produtos = list(dic_produtos.keys())
print(produtos)

# criar uma lista só dos valores a partir do dicionário:
precos = list(dic_produtos.values())
print(precos)

# contagem de itens do dicionário:
qtde_itens = len(dic_produtos)
print(qtde_itens)

# soma dos valores do dicionário:
sum_values = sum(dic_produtos.values())
print(sum_values)

# pegar o valor máximo do dicionário:
max_value = max(dic_produtos.values())
print(max_value)

# pegar o valor mínimo do dicionário:
min_value = min(dic_produtos.values())
print(min_value)

# média dos valores do dicionário:
media_values = (sum_values / qtde_itens)
print(media_values)