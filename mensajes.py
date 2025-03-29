from textos import textos


class Mensaje:
    def __init__(self, texto: str, prioridad: int, longitud_mensaje: int):
        self.texto: str = texto
        self.prioridad: int = prioridad
        self.longitud_mensaje: int = longitud_mensaje
        
    def __repr__(self):
        return f'Pioridad: {self.prioridad}; Longitud: {self.longitud_mensaje}'
        

def convertir_a_mensaje(textos):
    mensajes = []
    for i in range(len(textos)):
        longitud_mensaje = len(textos[i].split())

        mensaje = Mensaje(textos[i], 0, longitud_mensaje)
        mensajes.append(mensaje)
    return mensajes


mensajes = convertir_a_mensaje(textos)


def definir_prioridad(mensajes: list):
    palabras_clave = {
        "emergencia": 10, "urgente": 8, "fallo crítico": 9,
        "problema": 5, "consulta": 2, "duda": 1
    }
    
    for i in range(len(mensajes)):
        texto_copia = mensajes[i].texto
        texto_copia = texto_copia.lower()
        texto_copia = texto_copia.replace(',', '')
        texto_copia = texto_copia.replace('.', '')
        texto_copia = texto_copia.replace('?', '')
        texto_copia = texto_copia.replace('¿', '')

        for clave, valor in palabras_clave.items():
            if clave in texto_copia:
                mensajes[i].prioridad += valor


definir_prioridad(mensajes)
