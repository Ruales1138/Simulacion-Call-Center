import random


class Agente:
    def __init__(self, id: int, nivel_experiencia: str, estado: str, tiempo_de_respuesta: int):
        self.id: int = id
        self.nivel_experiencia: str = nivel_experiencia
        self.estado: str = estado
        self.tiempo_de_respuesta: int = tiempo_de_respuesta

    def __repr__(self):
        return f'Id: {self.id}, Experiencia: {self.nivel_experiencia}'


def crear_agentes(cantidad: int) -> list[Agente]:
    agentes = []
    niveles_de_experiencia = ['basico', 'intermedio', 'experto']
    estados = ['ocupado', 'disponible']

    for i in range(cantidad):
        id = i
        nivel_experiencia = random.choice(niveles_de_experiencia)
        estado = random.choice(estados)
        tiempo_de_respuesta = 0

        agente = Agente(id, nivel_experiencia, estado, tiempo_de_respuesta)
        agentes.append(agente)

    return agentes


agentes = crear_agentes(3)