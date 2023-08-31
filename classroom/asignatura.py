class Asignatura:

    def __init__(self, nombre, salon=None):
        self._nombre = nombre
        if salon == None:
            self._salon = "remoto"
            return
        self._salon = salon

    def __str__(self):
        return self._nombre + " " + self._salon
