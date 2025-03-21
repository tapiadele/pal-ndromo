class Pila: #defino la clase pila
    def __init__(self): #constructor
        self.items = [] #inicializo una lista vacía para guardar elementos en la pila

    #modificadores
    def apilar(self, item): #(push)
        self.items.append(item) #agregamos un item a la pila

    def desapilar(self): #para quitar y devolver el último elemento de la pila (pop)
        if not self.esta_vacia(): #verifica si la pila está vacía
            return self.items.pop() #si no lo está, devuelve con 'pop' el último elemento de ésta
        return None

    #consultores
    def esta_vacia(self):
        return len(self.items) == 0 #si la lista está vacía, devuelve True

def es_palindromo(palabra): #la función recibe una palabra como parámetro
    pila = Pila() #creamos la variable pila llamando a la clase Pila
    
    for letra in palabra: #recorremos cada letra de la palabra
        pila.apilar(letra) #las vamos apilando con 'apilar(letra)'; al desapilar van a estar en orden inverso (LIFO)
    
    palabra_invertida = "".join(pila.desapilar() for _ in range(len(palabra))) #se desapilan las letras y concatenan en un nuevo string (la palabra invertida)
    
    return palabra == palabra_invertida #compara la palabra original con la invertida; devuelve True si son iguales

# Solicitar entrada al usuario
palabra = input("Ingresa una palabra: ").lower() #paso la palabra ingresada por el usuario a minúsculas
if es_palindromo(palabra): #llama la función para verificar si la palabra es palíndromo; devuelve True si lo es
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")  #en caso de que no lo sea, devuelve False
