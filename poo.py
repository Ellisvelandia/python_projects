class Animal:
    def sonido(self):
        raise NotImplementedError("Subclase debe implementar el método 'sonido'")

class Perro(Animal):
    def sonido(self):
        return "Guau!"

class Gato(Animal):
    def sonido(self):
        return "Miau!"

def hacer_sonar(animal):
    return animal.sonido()

print(hacer_sonar(Perro()))  # Salida: Guau!
print(hacer_sonar(Gato()))   # Salida: Miau!








