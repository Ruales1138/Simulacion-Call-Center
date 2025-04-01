import time

class Mensaje:
    def __init__(self, texto: str, prioridad: int, longitud_mensaje: int):
        self.texto: str = texto
        self.prioridad: int = prioridad
        self.longitud_mensaje: int = longitud_mensaje
        
    def __repr__(self):
        return f'Pioridad: {self.prioridad}, Longitud: {self.longitud_mensaje}'
    

def buscar_textos(numero):
    with open(f"textos_{numero}.txt", "r", encoding="utf-8") as archivo:
        textos = archivo.readlines()
    return textos
        

def convertir_a_mensaje(textos: list[str]) -> list[Mensaje]:
    mensajes = []
    for i in range(len(textos)):
        longitud_mensaje = len(textos[i].split())

        mensaje = Mensaje(textos[i].strip(), 0, longitud_mensaje)
        mensajes.append(mensaje)
    return mensajes


textos = buscar_textos(3)
mensajes = convertir_a_mensaje(textos)


def definir_prioridad(mensajes: list[Mensaje]) -> None:
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
