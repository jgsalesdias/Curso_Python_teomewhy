def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """juros compostos servem para calcular retorno financeiro

    aporte: um número inteiro que represente o valor em reais

    taxa: Um número float entre 0 e 1 que represente o valor da taxa de juros

    anos: Um número inteiro >=1 que representa o tempo que o investimento terá liquidez
    """
    return aporte * (1 + taxa) ** anos

print(juros_compostos(aporte=1000, taxa=0.13, anos=4))