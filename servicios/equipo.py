from modelos.servicio import Servicio

class Equipo(Servicio):
    def calcular_costo(self, dias):
        return self.precio_base * dias

    def descripcion(self):
        return f"Equipo - ${self.precio_base}"
