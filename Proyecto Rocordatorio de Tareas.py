from datetime import datetime

class Tarea:
    def _init_(self, titulo, descripcion, fecha_vencimiento=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False

    def marcar_como_completada(self):
        self.completada = True

class GestorTareas:
    def _init_(self):
        self.tareas_pendientes = []
        self.tareas_completadas = []

    def agregar_tarea(self, tarea):
        self.tareas_pendientes.append(tarea)

    def mostrar_tareas_pendientes(self):
        if self.tareas_pendientes:
            print("Tareas Pendientes:")
            for i, tarea in enumerate(self.tareas_pendientes, 1):
                print(f"{i}. {tarea.titulo} - Descripción: {tarea.descripcion}", end="")
                if tarea.fecha_vencimiento:
                    print(f"Fecha de Vencimiento: {tarea.fecha_vencimiento}")
                else:
                    print(" sin fecha de vencimiento")
        else:
            print("no hay tareas pendientes.")

    def mostrar_tareas_completadas(self):
        if self.tareas_completadas:
            print("tareas Completadas:")
            for i, tarea in enumerate(self.tareas_completadas, 1):
                print(f"{i}. {tarea.titulo} - Descripción: {tarea.descripcion}")
        else:
            print("no hay tareas completadas.")

    def mostrar_todas_tareas(self):
        self.mostrar_tareas_pendientes()
        print("\n")
        self.mostrar_tareas_completadas()

    def marcar_como_completada(self, indice_tarea):
        if 0 < indice_tarea <= len(self.tareas_pendientes):
            tarea = self.tareas_pendientes.pop(indice_tarea - 1)
            tarea.marcar_como_completada()
            self.tareas_completadas.append(tarea)
            print(f"La tarea '{tarea.titulo}' ha sido marcada como completada y movida a la lista de tareas completadas.")
        else:
            print("indice de tarea inválido.")


gestor = GestorTareas()


while True:
    print("\n** Menú **")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_vencimiento_str = input("Ingrese la fecha de vencimiento (opcional - formato: YYYY-MM-DD): ")
        if fecha_vencimiento_str:
            fecha_vencimiento = datetime.strptime(fecha_vencimiento_str, '%Y-%m-%d')
        else:
            fecha_vencimiento = None
        tarea = Tarea(titulo, descripcion, fecha_vencimiento)
        gestor.agregar_tarea(tarea)
        print("Tarea agregada exitosamente.")

    elif opcion == "2":
        
        gestor.mostrar_todas_tareas()

    elif opcion == "3":
        
        gestor.mostrar_tareas_pendientes()
        indice_tarea_completada = int(input("ingrese el número de la tarea a marcar como completada: "))
        gestor.marcar_como_completada(indice_tarea_completada)

    elif opcion == "4":
        
        print("Saliendo del programa")
        break

    else:
        print("Opción no válida")