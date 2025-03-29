from mensajes import mensajes


class PriorityQueue:
    def __init__(self, priority):
        self.queue = []
        self.priority = priority
        
    def enqueue(self, mensaje):
        if self.priority == 'min':
            if len(self.queue) == 0:
                self.queue.append(mensaje)
            else:
                for i in range(len(self.queue)):
                    if mensaje.prioridad < self.queue[i].prioridad:
                        self.queue.insert(i, mensaje)
                        return
                self.queue.append(mensaje)
        
        if self.priority == 'max':
            if len(self.queue) == 0:
                self.queue.append(mensaje)
            else:
                for i in range(len(self.queue)):
                    if mensaje.prioridad > self.queue[i].prioridad:
                        self.queue.insert(i, mensaje)
                        return
                self.queue.append(mensaje)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def fist(self):
        return self.queue[0]
        

def organizar_cola(mensajes):
    q = PriorityQueue('max')
    for i in range(len(mensajes)):
        q.enqueue(mensajes[i])
    return q.queue


mensajes = organizar_cola(mensajes)