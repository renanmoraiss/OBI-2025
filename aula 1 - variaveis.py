# não precisa declarar o tipo da variável (ex: int, float, etc...), como é feito em C.

faturamento = 1000 
custo = 600

print("Antigo faturamento:", faturamento)

novas_vendas = 1000
faturamento += novas_vendas # faturamento = faturamento + novas_vendas
imposto = 0.15 * faturamento
lucro = faturamento - custo

print("Novo faturamento:", faturamento)
print("Custo:", custo)
print("Lucro:", lucro)
print("Imposto a ser pago", imposto)

mensagem = "O faturamento da Empresa foi de 2000" # string
print(mensagem)

teve_lucro = True # boolean
margem_lucro = (lucro / faturamento)
print("Margem de lucro:", margem_lucro)

# int = número inteiro
# float = número com casa decimal
# string = único caractere / palavra / frase
# boolean = True ou False (0 => False e 1 => True)

# Operadores Especiais:
# mod = %. Resto da divisão de um número pelo outro. Ex: 10 % 3 = 1
print(10 % 3)

anos = int(310 / 12)
print(anos, "anos")

meses = 310 % 12
print(meses, "meses")

# floor division = //. Pega a parte inteira de uma divisão.
print(310 // 12, "anos")