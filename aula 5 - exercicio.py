# criar um sistema de busca de produto em um dicionário
lista_produtos = {"ipad": 7000, "iphone": 5000, "airpod": 2000, "macbook": 12000}

produto_buscado = input("Qual produto deseja buscar: ")
produto_buscado = produto_buscado.strip() # remover os espaços vazios
produto_buscado = produto_buscado.lower() # deixar minúsculo (padrão do sistema)
verificar_produto = produto_buscado in lista_produtos

if verificar_produto == True:
    preco_produto_buscado = lista_produtos[produto_buscado]
    print(f"{produto_buscado} foi encontrado")
    print(f"{produto_buscado} está custando R${preco_produto_buscado:.2f}")
else:
    print(f"{produto_buscado} não existe no nosso sistema")