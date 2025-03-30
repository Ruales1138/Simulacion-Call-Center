from mensajes import mensajes
from agentes import agentes
print(agentes)
print('---------')


class PriorityQueue:
    def __init__(self, priority, tipo):
        self.queue = []
        self.priority = priority
        self.tipo = tipo
        
    def enqueue(self, elemento):

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
                        if elemento.nivel_experiencia < self.queue[i].nivel_experiencia:
                            self.queue.insert(i, elemento)
                            return
                    self.queue.append(elemento)

            if self.priority == 'max':
                if len(self.queue) == 0:
                    self.queue.append(elemento)
                else:
                    for i in range(len(self.queue)):
                        if elemento.nivel_experiencia > self.queue[i].nivel_experiencia:
                            self.queue.insert(i, elemento)
                            return
                    self.queue.append(elemento)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def fist(self):
        return self.queue[0]
        

def organizar_mensajes(mensajes):
    fila_mensajes = PriorityQueue('max', 'mensajes')
    for i in range(len(mensajes)):
        fila_mensajes.enqueue(mensajes[i])
    return fila_mensajes


def organizar_agentes(agentes):
    fila_agentes = PriorityQueue('max', 'agentes')
    for i in range(len(agentes)):
        fila_agentes.enqueue(agentes[i])
    return fila_agentes


fila_mensajes = organizar_mensajes(mensajes)
fila_agentes = organizar_agentes(agentes)