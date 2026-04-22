from modelos.cliente import Cliente
from modelos.reserva import Reserva
from servicios.sala import Sala
from servicios.equipo import Equipo
from servicios.asesoria import Asesoria
from utils.logger import registrar_log

clientes = []
reservas = []

print("=== SISTEMA SOFTWARE FJ ===")

# 🔷 CREACIÓN DE CLIENTES (válidos e inválidos)
try:
    clientes.append(Cliente("Jose Rugeles", "jose@mail.com"))
    clientes.append(Cliente("Ana Perez", "ana@mail.com"))

    # Error intencional
    clientes.append(Cliente("", ""))

except Exception as e:
    print("Error creando cliente:", e)
    registrar_log(f"Error cliente: {e}")

# 🔷 CREACIÓN DE SERVICIOS
servicios = [
    Sala("Sala VIP", 100),
    Equipo("Laptop", 50),
    Asesoria("Consultoría", 200)
]

# 🔷 SIMULACIÓN DE RESERVAS
for i in range(10):
    try:
        print(f"\n--- Operación {i+1} ---")

        cliente = clientes[0]
        servicio = servicios[i % 3]

        reserva = Reserva(cliente, servicio)

        # Probamos distintos parámetros
        if isinstance(servicio, Sala):
            costo = reserva.procesar(2, 0.1)
        elif isinstance(servicio, Equipo):
            costo = reserva.procesar(3)
        else:
            costo = reserva.procesar(1)

        reserva.confirmar()

        print(f"Reserva exitosa: {cliente.obtener_datos()}")
        print(f"Servicio: {servicio.descripcion()}")
        print(f"Costo: ${costo}")

        reservas.append(reserva)

    except Exception as e:
        print("Error en reserva:", e)
        registrar_log(f"Error en reserva {i}: {e}")

print("\n=== FIN DEL SISTEMA ===")
