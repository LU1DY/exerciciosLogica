lista = [12, 5, 23, -3, 0, 8, 42, -15, 7, 19]


def selectionSort(array):
    counter = 0
    while counter <= len(array):
        menor = array[counter]
        for indice, i in enumerate(array[counter:], start=counter):
            if i <= menor:
                menor = i
                item = indice
        array.pop(item)
        array.insert(counter, menor)
        if counter == len(array) - 1:
            break
        menor = array[counter]
        counter += 1
    return array

print(selectionSort(lista))

        
        

            
