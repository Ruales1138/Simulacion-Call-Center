import sys
sys.path.append('call_center')

from mensajes import crear_mensajes
from agentes import crear_agentes
from cola_prioritaria import organizar_mensajes, organizar_agentes
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

    print(fila_mensajes.queue)
    print('----------------------------------------------------------')
    print(fila_agentes.queue)
    print('----------------------------------------------------------')


def contar_archivos(carpeta):
    return len([f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))])

ruta = "datos"
numero_de_archivos = contar_archivos(ruta)

for i in range(numero_de_archivos):
    ejecutar_call_center(i+1)


