# ============================================
#   BASE DE DATOS SIMPLIFICADA
# ============================================

usuarios = {
    12345678: "Juan Perez",
    87654321: "Maria Gomez"
}

turnos_disponibles = {
    "Medicina Clínica": [(10, 6), (12, 6), (15, 6)],
    "Cardiología": [(11, 6), (20, 6)],
    "Dermatología": [(5, 7)]
}

# ============================================
#   ESTADO 0 — MENÚ INICIAL
# ============================================

def estado_0():
    print("===== BIENVENIDO AL SISTEMA DE TURNOS =====")
    print("1. Soy paciente nuevo")
    print("2. Ya soy paciente")
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        print("Error: ingrese solo números.")
        return estado_0()

# ============================================
#   ESTADO 1 — VALIDACIÓN / REGISTRO DE DNI
# ============================================

def estado_1(opcion):
    try:
        DNI = int(input("Por favor, ingrese su DNI sin puntos: "))
    except ValueError:
        print("Error: ingresar solo números.")
        return estado_1(opcion)

    if opcion == 1:  # Primera vez
        if DNI in usuarios:
            print("Este DNI ya está registrado.")
        else:
            nombre = input("Ingrese su nombre: ")
            usuarios[DNI] = nombre
            print(f"Registro exitoso. Bienvenido/a {nombre}!")
        return DNI

    elif opcion == 2:  # Ya soy paciente
        if DNI in usuarios:
            print(f"Bienvenido/a {usuarios[DNI]}!")
            return DNI
        else:
            print("DNI no encontrado. Debe registrarse primero.")
            return estado_1(1)

# ============================================
#   ESTADO 2 — SELECCIÓN DE ESPECIALIDAD
# ============================================

def estado_2():
    print("\n===== ESPECIALIDADES =====")
    lista = list(turnos_disponibles.keys())

    for i, esp in enumerate(lista, 1):
        print(f"{i}. {esp}")
    print(f"{len(lista)+1}. Volver al menú principal")

    try:
        opcion = int(input("Seleccione una especialidad: "))
    except ValueError:
        print("Error: ingrese solo números.")
        return estado_2()

    if opcion == len(lista)+1:
        return None

    if 1 <= opcion <= len(lista):
        especialidad = lista[opcion-1]
        if len(turnos_disponibles[especialidad]) > 0:
            print(f"Turnos disponibles en {especialidad}.")
            return especialidad
        else:
            print("No hay turnos disponibles.")
            return estado_2()
    else:
        print("Opción inválida.")
        return estado_2()

# ============================================
#   ESTADO 3 — SELECCIÓN DE FECHA
# ============================================

def estado_3(especialidad):
    try:
        dia = int(input("Ingrese el día deseado (solo números): "))
        mes = int(input("Ingrese el mes deseado (solo números): "))
    except ValueError:
        print("Error: ingrese solo números.")
        return estado_3(especialidad)

    encontrado = False
    for turno in turnos_disponibles[especialidad]:
        if turno == (dia, mes):
            encontrado = True
            break

    if encontrado:
        print("Turno disponible.")
        return dia, mes
    else:
        print("No hay turnos disponibles en esa fecha. Repita la operación.")
        return estado_3(especialidad)

# ============================================
#   ESTADO 4 — CONFIRMACIÓN FINAL
# ============================================

def estado_4(DNI, especialidad, dia, mes):
    nombre = usuarios[DNI]
    print("\n===== CONFIRMACIÓN DE TURNO =====")
    print(f"Paciente: {nombre}")
    print(f"Especialidad: {especialidad}")
    print(f"Fecha: {dia}/{mes}")
    print("Turno confirmado. ¡Gracias por utilizar el sistema!")

# ============================================
#   PROGRAMA PRINCIPAL
# ============================================

def main():
    # Estado 0
    opcion = estado_0()

    # Estado 1
    DNI = estado_1(opcion)

    # Estado 2
    especialidad = estado_2()
    if especialidad is None:
        print("Volviendo al menú principal...")
        return main()

    # Estado 3
    dia, mes = estado_3(especialidad)

    # Estado 4
    estado_4(DNI, especialidad, dia, mes)

main()



