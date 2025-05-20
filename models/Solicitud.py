class Solicitud:
    def __init__(self, fecha, rutConserje, estado):
        self._fecha = fecha
        self._rutConserje = rutConserje
        self._estado = estado
        
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @property
    def rutConserje(self):
        return self._rutConserje

    @rutConserje.setter
    def rutConserje(self, value):
        self._rutConserje = value
    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value