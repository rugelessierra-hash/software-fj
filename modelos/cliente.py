from utils.excepciones import ClienteInvalidoError

class Cliente:
    def __init__(self, nombre, email):
        if not nombre or not email:
            raise ClienteInvalidoError("Datos inválidos del cliente")
        self.__nombre = nombre
        self.__email = email

    def obtener_datos(self):
        return f"{self.__nombre} - {self.__email}"
