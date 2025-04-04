import sys
sys.path.append('call_center')
from mensajes import crear_mensajes
from agentes import crear_agentes
from cola_prioritaria import organizar_mensajes, organizar_agentes, PriorityQueue
import time
import os


agentes = crear_agentes(3)
fila_agentes = organizar_agentes(agentes)


def ejecutar_call_center(numero_de_archivo):

    mensajes = crear_mensajes(numero_de_archivo)
    fila_mensajes = organizar_mensajes(mensajes)

    print(f'📂 Archivo {numero_de_archivo}')
    print('----------------------------------------------------------')
    print(fila_mensajes.queue)
    print('----------------------------------------------------------')
    print(fila_agentes.queue)
    print('----------------------------------------------------------')

    def buscar_mas_cantidad(fila_mensajes):
        cola_aux = PriorityQueue('max', 'mensajes')
        contador = 1
        numero_actual = 0
        max = [0, 0]
        numero_anterior = 0

        for _ in range(len(fila_mensajes)):
            mensaje_actual = fila_mensajes.dequeue()
            numero_actual = mensaje_actual.prioridad
            cola_aux.enqueue(mensaje_actual)
            if numero_actual == numero_anterior:
                contador += 1
                numero_anterior = numero_actual
                if contador > max[1]:
                    max[0] = numero_actual
                    max[1] = contador
            else:
                contador = 1
                numero_anterior = numero_actual

        return max, cola_aux

    max, cola_aux = buscar_mas_cantidad(fila_mensajes)
    print(max)
    fila_mensajes = cola_aux

    def filtrar_cola(fila_mensajes, max):
        cola_aux_1 = PriorityQueue('max', 'mensajes')
        cola_aux_2 = PriorityQueue('max', 'mensajes')
        cola_aux_3 = PriorityQueue('max', 'mensajes')

        for _ in range(len(fila_mensajes)):
            mensaje_actual = fila_mensajes.dequeue()
            numero_actual = mensaje_actual.prioridad
            if numero_actual == max[0]:
                cola_aux_2.enqueue(mensaje_actual)
            else:
                cola_aux_1.enqueue(mensaje_actual)


        primer_mensaje = cola_aux_2.dequeue()
        ultimo_mensaje = cola_aux_2.dequeue()

        for _ in range(len(cola_aux_2)):
            ultimo_mensaje = cola_aux_2.dequeue()

        cola_aux_3.enqueue(primer_mensaje)
        cola_aux_3.enqueue(ultimo_mensaje)

        return cola_aux_1, cola_aux_3
    
    cola_aux_1, cola_aux_3 =filtrar_cola(fila_mensajes, max)
    print(cola_aux_3.queue)
    print('----------------------------------------------------------')

    fila_mensajes = cola_aux_3


    def definir_tiempo(fila_mensajes: object, fila_agentes: object) -> None:

        for _ in range(len(fila_mensajes.queue)):
            mensaje = fila_mensajes.dequeue()
            agente = fila_agentes.dequeue()
            longitud_mensaje = mensaje.longitud_mensaje
            peso_palabras_clave = mensaje.prioridad
            experiencia = agente.nivel_experiencia

            if experiencia == 'basico':
                factor_de_nivel = 1
            if experiencia == 'intermedio':
                factor_de_nivel = 0.75
            if experiencia == 'experto':
                factor_de_nivel = 0.5

            tiempo_estimado = (longitud_mensaje / 10) + (peso_palabras_clave / 2)
            ajuste_por_experiencia = tiempo_estimado * factor_de_nivel

            print('Mensaje:')
            print(mensaje.texto)
            print(mensaje)
            print('Agente:')
            print(agente)
            print(f'Tiempo de espera: {ajuste_por_experiencia}')
            print('----------------------------------------------------------')
            time.sleep(ajuste_por_experiencia)
            fila_agentes.enqueue(agente)

    definir_tiempo(fila_mensajes, fila_agentes)
    fila_mensajes = cola_aux_1

    print(fila_mensajes.queue)
    print('----------------------------------------------------------')
    print(fila_agentes.queue)
    print('----------------------------------------------------------')



def contar_archivos(carpeta):
    return len([f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))])

numero_de_archivos = contar_archivos('datos')

for i in range(numero_de_archivos):
    ejecutar_call_center(i+1)


