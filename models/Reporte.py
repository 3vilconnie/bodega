class Reporte:
    
    def __init__(self, fecha):
        self.fecha = fecha
        
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value