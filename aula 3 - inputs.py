faturamento = float(input("Faturamento da empresa: ")) # primeira forma de converter string para float 
faturamento = float(faturamento) # segunda forma de converter string para float

# por padrão, input vem sempre como string.
# para trabalhar com input com números, é necessário converter o input para int ou float.

custo = float(input("Custo da empresa: "))
custo = float(custo)

lucro = faturamento - custo

print(f"R${lucro:,.2f}")

saldo_bancario = input("Seu saldo bancário: ")
saldo_bancario = saldo_bancario.replace("R$", "").replace(",", ".")
saldo_bancario = float(saldo_bancario)
print(saldo_bancario)

imposto_a_ser_pago = 0.15 * saldo_bancario
print(imposto_a_ser_pago)

vendas_empresa_dia_um = int(input("Vendas do primeiro dia: "))
vendas_empresa_dia_dois = int(input("Vendas do segundo dia: "))

print(f"Vendas totais: {vendas_empresa_dia_um} + {vendas_empresa_dia_dois}")