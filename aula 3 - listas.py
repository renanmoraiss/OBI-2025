# lista em python pode ter dados de diferentes tipos, como por exemplo string e int.

lista_vendas = [100, 50, 1000, 800, 35] 

# pegar um item da lista:
primeiro_item_lista = lista_vendas[0]
print(f"Primeiro item da lista: {primeiro_item_lista}")

# pegar o tamanho da lista:
comprimento_lista = len(lista_vendas) # len de length (comprimento)
print(f"Comprimento da lista: {comprimento_lista}")

# somar todos os itens:
total_vendas = sum(lista_vendas) # sum = soma
print(f"Total de vendas: {total_vendas}")

# pegar o valor máximo:
max_vendas = max(lista_vendas) # max = máximo
print(f"Valor máximo: {max_vendas}")

# pegar o valor mínimo:
min_vendas = min(lista_vendas) # min = mínimo
print(f"Valor mínimo: {min_vendas}")

# pegar a média:
media_vendas = (total_vendas / comprimento_lista)
print(f"Media das vendas: {media_vendas}")

# encontrar um elemento (a posição do elemento na lista):
lista_produtos = ["iphone", "ipad", "apple watch", "airpod", "macbook"]
print("airpod" in lista_produtos) # True se encontrar e False se não encontrar.

posicao_airpod = lista_produtos.index("airpod")
print(f"Posição do airpod: {posicao_airpod}")

# pegar um pedaço da lista a partir do índice de um elemento:
pedaco_lista_produtos = lista_produtos[posicao_airpod:]
print(f"Pedaço da lista: {pedaco_lista_produtos}")

# editar um item da lista:
lista_precos = [5000, 7000, 3000, 1000, 10000]

lista_precos[0] = lista_precos[0] + (0.10 * lista_precos[0])
print(f"Lista de preços: {lista_precos}")

# remover um item da lista: (.remove e .pop)
lista_produtos.remove("macbook") # remove passa o valor do item
# item_removido = lista_produtos.pop(0) # pop passa a posição (index) do item e pode armazenar esse item numa variável
print(lista_produtos)
# print(item_removido) # exibe o item removido

# adicionar um item na lista: (.append e .extend)
lista_produtos.append("macbook") # append sempre adiciona um item no final da lista
print(lista_produtos)

lista_dois_produtos = ["PC", "air tag", "caixa de som"]
# adicionar os itens da lista_dois_produtos dentro da lista_produtos (estender a lista):
lista_produtos.extend(lista_dois_produtos)
print(lista_produtos)

# inserir um item em uma posição específica:
lista_produtos.insert(1, "airpod")
print(lista_produtos)

# contar quantas vezes um item aparece na lista:
contagem_item = lista_produtos.count("airpod")
print(contagem_item)

# ordenar uma lista: (maiúscula vem primeiro na tabela ASCII)
lista_precos.sort(reverse=True) # por padrão ordena do menor para maior, (reverse=True) para colocar do maior para menor.
print(lista_precos) 