import random


class Agente:
    def __init__(self, id, nivel_experiencia, estado, tiempo_de_respuesta):
        self.id = id
        self.nivel_experiencia = nivel_experiencia
        self.estado = estado
        self.tiempo_de_respuesta = tiempo_de_respuesta

    def __repr__(self):
        return f'Id: {self.id}, Experiencia: {self.nivel_experiencia}'


def crear_agentes(cantidad):
    agentes = []
    niveles_de_experiencia = [1, 2, 3]
    estados = ['ocupado', 'disponible']

    for i in range(cantidad):
        id = i
        nivel_experiencia = random.choice(niveles_de_experiencia)
        estado = random.choice(estados)
        tiempo_de_respuesta = 0

        agente = Agente(id, nivel_experiencia, estado, tiempo_de_respuesta)
        agentes.append(agente)

    return agentes


agentes = crear_agentes(10)