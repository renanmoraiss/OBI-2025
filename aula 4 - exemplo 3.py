# se as vendas forem menores do que 5000, o funcionário não ganha nada
# se as vendas forem entre 5000 e 15000, o funcionário ganha R$100 de bônus
# se as vendas maiores do que 15000, o funcionário ganha R$500 de bônus
# só recebe o bônus se as vendas da empresa forem maiores do que 10000

salario_funcionario = float(input("Salário do funcionário: "))
vendas_funcionario = int(input("Vendas do funcionário: "))
vendas_empresa = int(input("Vendas da empresa: "))

bonus_menor = 100
bonus_maior = 500

if vendas_empresa > 10000:
    if vendas_funcionario < 5000:
        print("Sem bônus")
    elif vendas_funcionario >= 5000 and vendas_funcionario <= 15000: # and = as duas condições devem ser verdadeiras
        salario_funcionario += bonus_menor
        print(f"Bônus de R${bonus_menor:.2f}")
    else:
        salario_funcionario += bonus_maior
        print(f"Bônus de R${bonus_maior:.2f}")
else:
    print("Sem bônus, porque a empresa não atingiu o número de vendas")

print(f"Novo salário: R${salario_funcionario:.2f}")