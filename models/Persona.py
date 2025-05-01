class Persona:
    def __init__(self, rut, nombre, apellido, email):
        self._rut = rut
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
    
    @property
    def nombre(self):
        return self._nombre

    @nombre
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido
    def apellido(self, value):
        self._apellido = value

    @property
    def email(self):
        return self._email

    @email
    def email(self, value):
        self._email = value