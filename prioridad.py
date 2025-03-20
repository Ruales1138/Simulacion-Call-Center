from textos import textos


class Mensaje:
    def __init__(self, texto: str, prioridad: int):
        self.texto: str = texto
        self.prioridad: int = prioridad
        
    def __repr__(self):
        return f'{self.texto} {self.prioridad}'
        

def convertir_a_mensaje(textos):
    mensajes = []
    for i in range(len(textos)):
        mensaje = Mensaje(textos[i], 1)
        mensajes.append(mensaje)
    return mensajes


mensajes = convertir_a_mensaje(textos)


def definir_prioridad(mensajes: list):
    palabras_clave = {
        "emergencia": 10, "urgente": 8, "fallo crítico": 9,
        "problema": 5, "consulta": 2, "duda": 1
    }
    
    for i in range(len(mensajes)):
        mensajes[i].texto = mensajes[i].texto.lower()
        mensajes[i].texto = mensajes[i].texto.replace(',', '')
        mensajes[i].texto = mensajes[i].texto.replace('.', '')
        mensajes[i].texto = mensajes[i].texto.replace('?', '')
        mensajes[i].texto = mensajes[i].texto.replace('¿', '')

        palabras = mensajes[i].texto.split()
        for j in range((len(palabras))):
            print(palabras[j])


    
    #palabras = texto.split()
    #for i in range(len(palabras)):
    #    for clave, valor in palabras_clave.items():
    #        if palabras[i] == clave:
    #            print('lo encontre')
    #            
    #    print(palabras[i])
    #return palabras

definir_prioridad(mensajes)
