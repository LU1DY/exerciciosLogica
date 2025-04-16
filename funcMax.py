lista = [10, -5, 3, -5, 7, 10, -2, 3, -8, 0, 7, 4, -1, -1, 90, -1, 12, 12, 12, -8, 6, 45]
def funcMax(lista):
    for i in lista:
        verificacaoMaior = [i >= x for x in lista]
        if False in verificacaoMaior:
            pass
        else:
            maior = i
    return maior


def funcMin(lista):
    for i in lista:
        verificacaoMenor = [i <= x for x in lista]
        if False in verificacaoMenor:
            pass
        else:
            menor = i
    return menor
    
        
maior = funcMax(lista)
menor = funcMin(lista)
print(f'O menor valor é {menor} e o menor é {maior}.')

