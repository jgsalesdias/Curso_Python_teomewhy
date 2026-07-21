# frases = {}

# while True:

#     frase = input("Entre com a frase: ")
#     if frase == "":
#         break
    
#     if frase not in frases:
#         frases[frase] = 1
#     else:
#         frases[frase] +=1

# for i in frases:
#     print(i, "->", frases[i])

dados = {
    "oi": 1,
    "ola": 10,
    "oi tudo bem": 3,
    "test": 2,
    "teste": 5,
}


items = list(dados.items())
items.sort(key=lambda x: x[-1], reverse=True)

for i, j in items:
    print(i, "->", j)