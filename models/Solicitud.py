class Solicitud:
    def __init__(self, fecha, Conserje):
        self.fecha = fecha
        self.Conserje = Conserje
        
    @property
    def fecha(self):
        return self._fecha

    @fecha
    def fecha(self, value):
        self._fecha = value

    @property
    def Conserje(self):
        return self._Conserje

    @Conserje
    def Conserje(self, value):
        self._Conserje = value