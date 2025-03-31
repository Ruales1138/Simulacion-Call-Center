from mensajes import mensajes
from agentes import agentes


class PriorityQueue:
    def __init__(self, priority: str, tipo: str):
        self.queue: list = []
        self.priority: str = priority
        self.tipo: str = tipo
        self.niveles_orden = {'experto': 3, 'intermedio': 2, 'basico': 1}
        
    def enqueue(self, elemento: object):

        if self.tipo == 'mensajes':

            if self.priority == 'min':
                if len(self.queue) == 0:
                    self.queue.append(elemento)
                else:
                    for i in range(len(self.queue)):
                        if elemento.prioridad < self.queue[i].prioridad:
                            self.queue.insert(i, elemento)
                            return
                    self.queue.append(elemento)

            if self.priority == 'max':
                if len(self.queue) == 0:
                    self.queue.append(elemento)
                else:
                    for i in range(len(self.queue)):
                        if elemento.prioridad > self.queue[i].prioridad:
                            self.queue.insert(i, elemento)
                            return
                    self.queue.append(elemento)

        if self.tipo == 'agentes':
            if self.priority == 'min':
                if len(self.queue) == 0:
                    self.queue.append(elemento)
                else:
                    for i in range(len(self.queue)):
                        if self.niveles_orden[elemento.nivel_experiencia] < self.niveles_orden[self.queue[i].nivel_experiencia]:
                            self.queue.insert(i, elemento)
                            return
                    self.queue.append(elemento)
            if self.priority == 'max':
                if len(self.queue) == 0:
                    self.queue.append(elemento)
                else:
                    for i in range(len(self.queue)):
                        if self.niveles_orden[elemento.nivel_experiencia] > self.niveles_orden[self.queue[i].nivel_experiencia]:
                            self.queue.insert(i, elemento)
                            return
                    self.queue.append(elemento)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def fist(self):
        return self.queue[0]
        

def organizar_mensajes(mensajes: list[object]) -> PriorityQueue:
    fila_mensajes = PriorityQueue('max', 'mensajes')
    for i in range(len(mensajes)):
        fila_mensajes.enqueue(mensajes[i])
    return fila_mensajes


def organizar_agentes(agentes: list[object]) -> PriorityQueue:
    fila_agentes = PriorityQueue('max', 'agentes')
    for i in range(len(agentes)):
        fila_agentes.enqueue(agentes[i])
    return fila_agentes


fila_mensajes = organizar_mensajes(mensajes)
fila_agentes = organizar_agentes(agentes)