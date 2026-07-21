lista = [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

numero = int(input("Entre com um número: "))
count_numero = 0

for i in lista:
    if numero == i:
        count_numero +=1
    
print(count_numero)