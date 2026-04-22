from modelos.servicio import Servicio

class Sala(Servicio):
    def calcular_costo(self, horas, descuento=0):
        costo = self.precio_base * horas
        return costo - (costo * descuento)

    def descripcion(self):
        return f"Sala por horas - ${self.precio_base}"
