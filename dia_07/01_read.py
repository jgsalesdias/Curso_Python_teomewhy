nome_arquivo = 'historia.txt'

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)



# open_file = open(nome_arquivo)

# conteudo = open_file.read()

# print(conteudo)

# open_file.close()