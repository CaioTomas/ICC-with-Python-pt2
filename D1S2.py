def conta_letras(frase, contar="vogais"):
    total = 0
    vogais = ['a', 'e', 'i', 'o', 'u']
    frase = frase.lower()
    if contar == "vogais":
        for i in range(len(frase)):
            if frase[i] in vogais:
                total += 1
    else:
        for i in range(len(frase)):
            if frase[i] not in vogais and frase[i] != ' ':
                total += 1
    return total