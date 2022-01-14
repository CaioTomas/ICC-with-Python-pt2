def dimensoes(matriz):
    
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    
    return (num_linhas, num_colunas)

def soma_matrizes(m1, m2):
    
    if dimensoes(m1) == dimensoes(m2):
        soma = []
        for i in range(dimensoes(m1)[0]):
            linha_soma = []
            for j in range(dimensoes(m1)[1]):
                linha_soma.append(m1[i][j] + m2[i][j])
            soma.append(linha_soma)
        
        return soma
    
    else:
        return False