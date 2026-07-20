soma = 0
qtde_entradas = 4

for i in range(qtde_entradas):
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura

print("Soma das alturas:", soma)