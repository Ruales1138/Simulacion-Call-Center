from cola_prioritaria import fila_mensajes, fila_agentes
print(fila_mensajes.queue)
print('-----')
print(fila_agentes.queue)
print('-----')


def definir_tiempo(fila_mensajes, fila_agentes):
    for i in range(len(fila_agentes.queue)):
        mensaje = fila_mensajes.dequeue()
        agente = fila_agentes.dequeue()
        longitud_mensaje = mensaje.longitud_mensaje
        peso_palabras_clave = mensaje.prioridad
        experiencia = agente.nivel_experiencia
        
        if experiencia == 'basico':
            factor_de_nivel = 1
        if experiencia == 'intermedio':
            factor_de_nivel = 0.25
        if experiencia == 'experto':
            factor_de_nivel = 0.5

        tiempo_estimado = (longitud_mensaje / 10) + (peso_palabras_clave / 2)
        ajuste_por_experiencia = tiempo_estimado * factor_de_nivel
        
        print(mensaje)
        print(agente)
        print(ajuste_por_experiencia)


definir_tiempo(fila_mensajes, fila_agentes)
print(fila_mensajes.queue)
print('-----')
print(fila_agentes.queue)
print('-----')


