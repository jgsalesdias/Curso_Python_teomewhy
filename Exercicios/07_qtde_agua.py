# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

tipo_garrafa = input("Digite 1 para comprar água natural ou 2 para água com gás: ")

valor_item = 0
if tipo_garrafa == "1":
    valor_item = 1.5
elif tipo_garrafa == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Entre com a porra da opção correta, por favor")

else:
    qtde_garrafas = int(input("Quantas garrafas? "))
    valor_total = valor_item * qtde_garrafas
    print("Sua conta deu: R$", valor_total)



