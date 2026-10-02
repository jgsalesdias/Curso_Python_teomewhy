import random

def get_input():
     while True:    
        try:
            num_user = int(input("Digite um número: "))
     
        except ValueError as err:
            print("Valor inválido")
            continue
     
        if 1 <= num_user <= 15:
            return num_user
     
        print("O valor deve ser entre 1 e 15")

numero_sorteio = random.randint(1,15)

for i in range(3):

    num_user = get_input()

    if numero_sorteio == num_user:
            print("Parabéns! Você acertou!")
        
    elif numero_sorteio > num_user:
            print("O número é maior que o sorteado! ")
    else:
            print("O número e menor que o sorteado! ")

else:
    print("Suas tentativas acabaram")
