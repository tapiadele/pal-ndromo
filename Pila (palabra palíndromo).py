class Pila: #waska #y a la abuela? soy la abueeeeela
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

def es_palindromo(palabra):
    pila = Pila()
    
    for letra in palabra:
        pila.apilar(letra)
    
    palabra_invertida = "".join(pila.desapilar() for _ in range(len(palabra)))
    
    return palabra == palabra_invertida

# Solicitar entrada al usuario
palabra = input("Ingresa una palabra: ").lower()
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
