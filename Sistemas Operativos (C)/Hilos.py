import threading
import time

def tarea(nombre):
    for i in range(5):
        print(f"Hilo {nombre}: ejecución {i+1}")
        time.sleep(1)

hilo1 = threading.Thread(target=tarea, args=("A",))
hilo2 = threading.Thread(target=tarea, args=("B",))
hilo3 = threading.Thread(target=tarea, args=("C",))

hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()

print("Ejecución finalizada")
