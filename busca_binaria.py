vetor = [12, -3, 25, -17, 8, -42, 0, 19, -1, 33,
         -12, 7, -25, 4, 18, -9, 2, -30, 22, -6,
         10, -11, 5, -7, 29, -22, 14, -2, 3, -15, 1, 39, 74, 292, 284, -2, 23, 903, 3856, 846, 3857, 294, 903, 905, 9043, 9753]

def busca_binaria(lista, chave):
    inicio = 0
    fim = len(vetor) - 1

    meio = 0
    counter = 0
    while inicio < fim:
        meio = (inicio + fim) // 2
        lista = sorted(lista)
        if lista[meio] == chave:
            return f'O índice do valor {chave} é {meio}, foi encontrado depois de {counter} tentativas.'
        else:
            if lista[meio] > chave:
                fim = meio - 1
            else:
                inicio = meio + 1
        counter += 1
    
    return f'O valor {chave} não foi encontrado, o algoritmo executou {counter} vezes.'
    

chave = int(input('Informe o valor que deseja buscar: '))
print(busca_binaria(vetor, chave))


