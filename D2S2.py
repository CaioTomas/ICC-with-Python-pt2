def primeiro_lex(lista):
    menor = lista[0]
    
    for palavra in lista:
        if palavra < menor:
            menor = palavra
            
    return menor