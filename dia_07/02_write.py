txt = "meu novo arquivo!"

nome_arquivo = "historia2.txt"

with open(nome_arquivo, mode="w") as open_file:
    open_file.write(txt)
