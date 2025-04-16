lista = [10, -5, 3, -5, 7, 10, -2, 3, -8, 0, 7, 4, -1, -1, -1, 12, -8, 6]

def funcLen(lista):
    counter = 0
    while lista[counter] != lista[-1]:
        counter += 1
    return counter + 1

# print(funcLen(lista))

def funcIn(num, lista):
    counter = 0
    while counter < funcLen(lista):
        if num == lista[counter]:
            return True
        counter += 1
    return False


print(funcIn(10, lista))