#Escribir una clase en python llamada rectangulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (self.base + self.altura) * 2
    
    def __str__(self):
        return f"Base: {self.base} Altura: {self.altura}"
    
    def __del__(self):
        print("Se ha eliminado el objeto")

rectangulo = Rectangulo(5, 10)
print(rectangulo.area())
print(rectangulo.perimetro())
print(rectangulo)
del(rectangulo)






