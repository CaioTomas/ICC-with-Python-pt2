def menor_nome(nomes):
    menor = nomes[0].lower().strip()
    for nome in nomes:
        nome = nome.lower().strip()
        if len(nome) < len(menor):
            menor = nome
            
    return menor.capitalize()