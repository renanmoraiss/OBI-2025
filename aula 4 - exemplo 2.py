# se as vendas forem menores do que 5000, o funcionário não ganha nada
# se as vendas forem entre 5000 e 15000, o funcionário ganha R$100 de bônus
# se as vendas maiores do que 15000, o funcionário ganha R$500 de bônus

salario_funcionario = float(input("Salário do funcionário: "))
numero_vendas = int(input("Número de vendas do funcionário: "))
bonus_menor = 100
bonus_maior = 500

if numero_vendas < 5000:
    print(f"O funcionário não ganha bônus")
else: # aninhamento de if
    if numero_vendas <= 15000:
        salario_funcionario += bonus_menor
        print(f"O funcionário ganha R${bonus_menor} de bônus")
    else:
        salario_funcionario += bonus_maior
        print(f"O funcionário ganha R${bonus_maior} de bônus")

print(f"Novo salário: R${salario_funcionario:.2f}")