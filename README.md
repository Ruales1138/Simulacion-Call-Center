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

# 2. Cálculo de Prioridad del Mensaje
- Se implementará una heurística personalizada que evalúe la urgencia de cada mensaje.
- Se usará un diccionario de palabras clave, donde cada término tiene un peso específico.
- La prioridad se calculará sumando los valores de las palabras encontradas en el mensaje.
- Ejemplo de diccionario de palabras clave: 
palabras_clave = {
    "emergencia": 10, "urgente": 8, "fallo crítico": 9,
    "problema": 5, "consulta": 2, "duda": 1
}
- Se debe recorrer el contenido del mensaje y sumar los valores encontrados para determinar la prioridad.
- Este valor continuo determinará la posición del mensaje en la cola de prioridad.

# 3. Gestión de Agentes de Atención

Los agentes son los encargados de atender los mensajes en la medida en que se desocupen.

Cada agente tendrá características propias que afectarán el tiempo que tarda en atender un caso.

### Creación de Objetos de Tipo Agente:

Cada agente debe ser representado como un objeto con atributos específicos, incluyendo:

- id: Identificador único del agente.
- nivel_experiencia: Puede ser básico, intermedio o experto.
- estado: Puede estar ocupado o disponible.
- tiempo_de_respuesta: Calculado con base en su experiencia y la dificultad del mensaje.

### Ejemplo de niveles de experiencia y su impacto en el tiempo de respuesta:
Nivel
Reducción en tiempo de respuesta
Básico
Sin reducción (100%)
Intermedio
Reduce 25% del tiempo esperado
Experto
Reduce 50% del tiempo esperado





