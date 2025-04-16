lista = [10, -5, 3, -5, 7, 10, -2, 3, -8, 0, 7, 4, -1, -1, -1, 12, -8, 6]

def ordenarSemMetodos(lista):
    tamanho_lista = len(lista)
    contador = 0
    teste = lista[:]
    ordenada = []
    while contador < tamanho_lista:
        for i in lista:
            teste2 = [x for x in teste if not x in ordenada]
            verificacao = [i <= x for x in teste2]
            if i in ordenada:
                pass
            else:
                if False in verificacao:
                    pass
                else:
                    ordenada.insert(0, i)
                    contador += 1
                    tamanho = 0
                    repetidos = [i == x for x in lista]
                    for x in repetidos:
                        if x == True:
                            tamanho += 1
                    if tamanho > 1:
                        for _ in range(tamanho - 1):
                            ordenada.insert(0, i)
                            contador += 1
                
    return ordenada


print(ordenarSemMetodos(lista))



