from prioridad import mensajes
print(mensajes)

class Queue:
    def __init__(self, priority):
        self.queue = []
        self.priority = priority