import threading  # Importa el módulo threading para manejar hilos

contador = 0  # Variable compartida entre los hilos
lock = threading.Lock()  # Crea un bloqueo para evitar condiciones de carrera

def incrementar():
    global contador  # Indica que la variable contador es global
    for _ in range(1000000):  # Bucle que incrementa el contador un millón de veces
        with lock:  # Bloquea la variable para que solo un hilo la modifique a la vez
            contador += 1  # Incrementa el valor del contador en 1

# Crea dos hilos que ejecutarán la función incrementar
hilo1 = threading.Thread(target=incrementar)
hilo2 = threading.Thread(target=incrementar)

hilo1.start()  # Inicia la ejecución del primer hilo
hilo2.start()  # Inicia la ejecución del segundo hilo

hilo1.join()  # Espera a que el primer hilo termine su ejecución
hilo2.join()  # Espera a que el segundo hilo termine su ejecución

# Muestra el valor final del contador después de que ambos hilos hayan terminado
print("Valor final del contador:", contador)


