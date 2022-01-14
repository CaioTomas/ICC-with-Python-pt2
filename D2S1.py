def dimensoes(matriz):
    
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    
    return (num_linhas, num_colunas)

def sao_multiplicaveis(m1, m2):
    
    if dimensoes(m1)[1] == dimensoes(m2)[0]:
        return True
    else:
        return False