dados_teo = {
    "sobrenome":"calvo",
    "nome":"téo", 
    "filhos":True,
    "formacao":["Estatística", "bigdata datascience"],
    "cargos":[
        {"nome":"ds jr.", "empresa":"tapps"},
        {"nome":"ds pl.", "empresa":"sas"},
        {"nome":"ds sr.", "empresa":"boticario"},
        {"nome":"sd espec.", "empresa":"via varejo"},
    ]
}

#acessando os elementos nos dicionários e listas
# print(dados_teo["cargos"][-1]["empresa"])

dados_teo["estado civil"] = "casado"

#.keys() para acessar as chaves do dicionário
dados_teo.keys()

#.values para acessar os VALORES das chaves do dicionário
dados_teo.values()

#.items() é uma lista de tuplas que possuem as chaves e valores do dicionário
dados_teo.items()

#percorrer os itens de um dicionário:
# for i in dados_teo:
#     print(i, "->", dados_teo[i])


for chave, valor in dados_teo.items():
    print(chave, "->", valor)

    