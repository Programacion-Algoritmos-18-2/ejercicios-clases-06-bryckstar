from paquete.modelado import *  # Se importan todas las clases de modelado

# Se crean los objetos de cada clase
a = Entrenador("Jose")
b = Futbolista("Antonio")
c = MedicoEquipo("Ramon")
d = PresidenteEquipo("Francisco")

lista = [a, b, c, d]  # Se crea una lista que almacene los objetos creados
for l in lista:  # Se crea el ciclo para recorrer la lista
    l.entrenamiento()  # Se llama al metodo entrenamiento de la clase abstracta
