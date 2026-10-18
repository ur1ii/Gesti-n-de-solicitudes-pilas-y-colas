cola_pendientes = []
pila_historial = []
siguiente_id = 1


def mostrar_estado():
    print("\nPendientes:", cola_pendientes)
    print("Historial:", pila_historial)

def registrar_solicitud(cliente, asunto):
    global siguiente_id
    if not cliente.strip() or not asunto.strip():
        return None

    solicitud = {
        "id": siguiente_id,
        "cliente": cliente.strip(),
        "asunto": asunto.strip(),
        "estado": "pendiente"
    }
    cola_pendientes.append(solicitud)
    siguiente_id += 1
    return solicitud


registrar_solicitud("Ana", "No conecta a Wi-Fi")
registrar_solicitud("Luis", "Impresora sin papel")
registrar_solicitud("Sofía", "Equipo lento")
mostrar_estado()

def atender_siguiente():
    if not cola_pendientes:
        return None

    solicitud = cola_pendientes.pop(0)
    solicitud["estado"] = "atendida"
    pila_historial.append(solicitud)
    return solicitud


print("Atendida:", atender_siguiente())
mostrar_estado()

def deshacer_ultima_atencion():
    if not pila_historial:
        return None

    solicitud = pila_historial.pop()
    solicitud["estado"] = "pendiente"
    cola_pendientes.insert(0, solicitud)
    return solicitud

print("Restaurada:", deshacer_ultima_atencion())
mostrar_estado()

def consultar_siguiente():
    if not cola_pendientes:
        return None
    return cola_pendientes[0]

def buscar_solicitud(id_solicitud):
    for solicitud in cola_pendientes:
        if solicitud["id"] == id_solicitud:
            return "Cola pendientes"
    for solicitud in pila_historial:
        if solicitud["id"] == id_solicitud:
            return "Historial"
    return None

def cancelar_pendiente(id_solicitud):
    for i, solicitud in cola_pendientes:
        if solicitud["id"] == id_solicitud:
            return cola_pendientes.pop(i)
    return None

def deshacer_varias(cantidad):
    if not isinstance(cantidad, int) or cantidad <= 0:
        print("La cantidad debe ser un entero positivo mayor a 0.")
        return 0
    restauradas = 0
    for _ in range(cantidad):
        resultado = deshacer_ultima_atencion()
        if resultado is None:
            break  
        restauradas += 1

    return restauradas

def obtener_estadisticas():
    pendientes = len(cola_pendientes)
    historial = len(pila_historial)
    total_unicas = pendientes + historial
    
    return {
        "pendientes": pendientes,
        "historial": historial,
        "total_unicas": total_unicas
    }

def ejecutar_menu():
    while True:
        print("\n1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Deshacer última atención")
        print("4. Mostrar estado")
        print("5. Salir")
        print("6. buscar solicitud")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cliente = input("Cliente: ")
            asunto = input("Asunto: ")
            resultado = registrar_solicitud(cliente, asunto)
            print("Registrada:", resultado if resultado else "Datos inválidos")
        elif opcion == "2":
            print("Atendida:", atender_siguiente())
        elif opcion == "3":
            print("Restaurada:", deshacer_ultima_atencion())
        elif opcion == "4":
            mostrar_estado()
        elif opcion == "5":
            break
        elif opcion == "6":
            print("Ingresa el id: ", buscar_solicitud())
        else:
            print("Opción inválida")


if __name__ == "__main__":
    ejecutar_menu()