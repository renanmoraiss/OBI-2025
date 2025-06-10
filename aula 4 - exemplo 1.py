# verificar se um item digitado pelo usuário já está na lista
# se não tiver, deve adicioná-lo
# se tiver, deve informar que já existe

lista_produtos = ["iphone", "ipad", "airpod"]
novo_produto = input("Digite um novo produto: ")

if novo_produto in lista_produtos:
    print(f"{novo_produto} já existe!")
else:
    print(f"{novo_produto} cadastrado!")
    lista_produtos.append(novo_produto)

print(lista_produtos)