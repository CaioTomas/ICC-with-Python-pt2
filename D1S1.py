def imprime_matriz(matriz):
    
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    
    for i in range(num_linhas):
        linha = ''
        for j in range(num_colunas):
            if j == num_colunas - 1:
                linha = linha + str(matriz[i][j])
            else:
                linha =  linha + str(matriz[i][j]) + ' '
            
        print(linha)