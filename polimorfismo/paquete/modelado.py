import abc  # Se importa la libreria necesaria para crear clases abstractas


# Se crea la clase padre abstracta
class PersonaEquipo(metaclass=abc.ABCMeta):
    """
        se define la clase abstracta
    """

    # __metaclass__ = abc.ABCMeta

    def __init__(self, n):
        self.nombre = n

    def setNombre(self, n):
        self.nombre = n

    def getNombre(self):
        return self.nombre

    # Se crea el metodo abstracto
    @abc.abstractmethod
    def entrenamiento(self):
        pass


class Entrenador(PersonaEquipo):

    def __init__(self, n):
        super(Entrenador, self).__init__(n)
        self.codigo_entrenado = ''

    def setCodigoEntrenador(self, codigoEntrenado):
        self.codigoEntrenado = codigoEntrenado

    def getCodigoEntrenador(self):
        return self.codigoEntrenado

    def entrenamiento(self):
        print("%s es un entrenador, que dirige el entrenamiento" % (self.getNombre()))


class Futbolista(PersonaEquipo):

    def __init__(self, n):
        super(Futbolista, self).__init__(n)
        self.posicionCampo = ""

    def setPosicionCampo(self, posicionCampo):
        self.posicionCampo = posicionCampo

    def getPosicionCampo(self):
        return self.posicionCampo

    # Se crea un metodo abstracto como en la clase padre para poder iterar entre las clases
    def entrenamiento(self):
        print("Yo %s, Futbolista, hago Practica en el entrenamiento " % (self.getNombre()))


class MedicoEquipo(PersonaEquipo):

    def __init__(self, n):
        super(MedicoEquipo, self).__init__(n)
        self.titulo = ''

    def setTitulo(self, n):
        self.titulo = n

    def getTitulo(self):
        return self.titulo

    # Se crea un metodo abstracto como en la clase padre para poder iterar entre las clases
    def entrenamiento(self):
        print('Yo %s, medico, atiendo a los jugadores en el entrenamiento.' % (self.getNombre()))


class PresidenteEquipo(PersonaEquipo):

    def __init__(self, n):
        super(PresidenteEquipo, self).__init__(n)
        self.num_propiedades = ''

    def setNum_propiedades(self, n):
        self.num_propiedades = ''

    def getNum_propiedades(self):
        return self.num_propiedades

    # Se crea un metodo abstracto como en la clase padre para poder iterar entre las clases
    def entrenamiento(self):
        print("Yo %s, presidente, pongo el dinero para el entrenamiento." % (self.getNombre()))
