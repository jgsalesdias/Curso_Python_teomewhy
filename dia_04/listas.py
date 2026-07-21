idades = [28, 42, 43, 35, 39, 28, 38]

# print(idades)

# teo = ["téo", "calvo", 32, 1, "casado", 2342.98]

# print(teo[3])

#sum() para somar os valores
sum(idades)

# media = sum(idades) / len(idades)
# print(media)

#menor idade
min(idades)

#maior idade
max(idades)

teo = ["téo calvo", 32, True, "casado",
       ["estagiario", "ds jr.", "ds pl", "ds sr.","head"], 
       [1500, 4000, 4500, 6500, 10000],
       ["ana", "maria", "claudia"]]

# tamanho = len(teo)
# pos = tamanho -1
# print(teo[pos])

# -1 sempre irá acessar o último elemento de uma lista
# print(teo[-1][-1])

#fatiamento de listas
teo[0:4]

print(teo[4][-2:])