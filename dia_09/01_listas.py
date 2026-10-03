x = []
for i in range(1,101):
    x.append(i)

y = [i for i in range(1,101)]


def eh_par(x):
    return x % 2 == 0

z = [eh_par(i) for i in range(1,101)]

w = [i for i in range(1,101) if eh_par(i)]