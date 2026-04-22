from modelos.servicio import Servicio

class Asesoria(Servicio):
    def calcular_costo(self, horas):
        return self.precio_base * horas

    def descripcion(self):
        return f"Asesoría - ${self.precio_base}"
