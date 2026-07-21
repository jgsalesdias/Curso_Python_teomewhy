# idades = [17, 32, 56, 87]

# print(idades)

# #o método .append é utilizado para adicionar itens a uma lista já existente
# idades.append(32)

# print(idades)

idades = []

while True:
    idade = input("Entre com a idade: ")

    if idade == "":
        break

    idades.append(int(idade))

print(idades)

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print("MEDIA:", media)
print("MINIMO:", minimo)
print("maximo:", maximo)
print("quantidade:", qtde)