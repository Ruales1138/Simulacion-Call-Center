# Práctica de Colas de Prioridad
# Simulación de un Call Center con Cola de Prioridad
# Descripción General

Los estudiantes deben implementar un sistema de atención de llamadas usando una cola de prioridad, donde los mensajes de los clientes son analizados para determinar su prioridad de atención.


Los agentes tienen diferentes niveles de experiencia y responderán los casos en la medida en que se desocupen.


El sistema funcionará de manera continua a demanda, leyendo nuevos mensajes desde una carpeta y encolándolos con una prioridad dinámica basada en su contenido.

# Requisitos del Sistema

# 1. Procesamiento de mensajes de clientes
- Se leerán mensajes aleatorios desde archivos de una carpeta.
- Cada mensaje tendrá un nivel de prioridad basado en su contenido.
- La prioridad será un valor continuo, calculado con una heurística basada en la presencia de palabras clave.

