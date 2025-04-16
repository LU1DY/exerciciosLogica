lista = [10, -5, 3, -5, 7, 10, -2, 3, -8, 0, 7, 4, -1, -1, -1, 12, -8, 6]

def funcLenght(lista):
    tamanho = 0
    for _ in lista:
        tamanho += 1

    return tamanho

print(funcLenght(lista))
