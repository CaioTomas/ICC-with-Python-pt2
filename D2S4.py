def ordena(lista):    
    for i in range(len(lista) - 1):
        pos_min = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[pos_min]:
                pos_min = j
        lista[i], lista[pos_min] = lista[pos_min], lista[i]
    return lista