def soma(a:float, b:float, *args)->float:
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a,b,*args) / (len(args)+2)

a = int(input("Entre com o valor de a: "))
b = int(input("Entre com o valor de b: "))
c = int(input("Entre com o valor de c: "))


print(media(a,b,c))