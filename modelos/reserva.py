from utils.logger import registrar_log

class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "pendiente"

    def confirmar(self):
        self.estado = "confirmada"
        registrar_log("Reserva confirmada")

    def procesar(self, *args):
        try:
            return self.servicio.calcular_costo(*args)
        except Exception as e:
            registrar_log(f"Error en cálculo: {e}")
            raise
