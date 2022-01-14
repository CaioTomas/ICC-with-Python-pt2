def incomodam(n):
    if n <= 0:
        return ''
    
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n):
    bla = True
    if n < 1:
        return ''
    elif n == 1:
        return "Um elefante incomoda muita gente\n"
        bla = False
    
    #if n > 1:
        #bla = elefantes(n-1) + str(n) + ' elefantes incomodam muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'
        #return elefantes(n-1) + str(n) + ' elefantes incomodam muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'
        #return bla.rstrip('\n')
        
    if bla == True:
        return elefantes(n-1) + str(n) + ' elefantes incomodam muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'
    else:
        return elefantes(n-1) + str(n) + ' elefantes incomodam muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + 'muito mais'
    
print(elefantes(3))