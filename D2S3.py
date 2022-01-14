class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        perimetro = self.a + self.b + self.c
        return perimetro
    
    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return "equilátero"
        elif self.a == self.b and self.b != self.c or self.a != self.b and self.b == self.c or self.a == self.c and self.b != self.c:
            return "isósceles"
        else:
            return "escaleno"
        
    def retangulo(self):
        lados = [float(self.a), float(self.b), float(self.c)]
        lados.sort()
        
        if (lados[2]**2 == lados[0]**2 + lados[1]**2):
            return True
        else:
            return False
        
    def semelhantes(self, triangulo):
        tri1 = [self.a, self.b, self.c]
        tri2 = [triangulo.a, triangulo.b, triangulo.c]
        tri1.sort()
        tri2.sort()
        
        if tri1[0]/tri2[0] == tri1[1]/tri2[1] and tri1[1]/tri2[1] == tri1[2]/tri2[2]:
            return True
        else:
            return False