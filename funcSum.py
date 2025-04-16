lista = [10, -5, 3, -5, 7, 10, -2, 3, -8, 0, 7, 4, -1, -1, -1, 12, -8, 6]

def funcSum(lista):
    total = 0
    for i in lista:
        total += i

    return total


print(funcSum(lista))