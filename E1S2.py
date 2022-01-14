def maiusculas(frase):
    string = ''
    for i in range(len(frase)):
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
            string = string + frase[i]
            
    return string