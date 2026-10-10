# ============================================================
# Sistema de calificaciones usando vectores (listas) en Python.
# Autor: Darving Arturo Jimenez Gomez.
# Asignatura: Introducción a la Programación para el Itla.
# Asginacion del Capítulo IX: Arreglos y Vectores.
# ============================================================

NOTA_MINIMA = 70   # nota mínima para aprobar (ajústala si tu curso usa otra)

# Vectores paralelos: la posición i de "nombres" corresponde
# a la posición i de "calificaciones".
nombres = ["Ana", "Luis", "Carla", "Miguel", "Sofía"]
calificaciones = [85, 67, 92, 74, 58]

print("=== SISTEMA DE CALIFICACIONES ===")
print("Estudiantes:", nombres)
print("Vector inicial de calificaciones:", calificaciones)

opcion = 0
while opcion != 8:
    print("\n----------- MENÚ -----------")
    print("1. Mostrar todas las calificaciones")
    print("2. Consultar una calificación por su número")
    print("3. Calcular el promedio")
    print("4. Ver la calificación más alta y la más baja")
    print("5. Contar aprobados y reprobados")
    print("6. Buscar un estudiante por nombre")
    print("7. Modificar una calificación")
    print("8. Salir")

    entrada = input("Elija una opción (1-8): ")
    if entrada.isdigit():
        opcion = int(entrada)
    else:
        opcion = 0          # entrada inválida

    if opcion == 1:
        print("\n--- Lista de estudiantes ---")
        for i in range(len(calificaciones)):
            if calificaciones[i] >= NOTA_MINIMA:
                estado = "Aprobado"
            else:
                estado = "Reprobado"
            print(f"{i + 1}. {nombres[i]}: {calificaciones[i]} ({estado})")
        print("Vector actual:", calificaciones)

    elif opcion == 2:
        entrada = input(f"Número del estudiante (1 a {len(calificaciones)}): ")
        if entrada.isdigit() and 1 <= int(entrada) <= len(calificaciones):
            indice = int(entrada) - 1      # la posición 1 es el índice 0
            print(f"{nombres[indice]} (índice {indice}) tiene {calificaciones[indice]}")
        else:
            print("Número fuera de rango: no existe ese estudiante.")

    elif opcion == 3:
        suma = sum(calificaciones)
        promedio = suma / len(calificaciones)
        print(f"Suma de notas: {suma}")
        print(f"Promedio del grupo: {promedio:.2f}")

    elif opcion == 4:
        mayor = calificaciones[0]
        menor = calificaciones[0]
        pos_mayor = 0
        pos_menor = 0
        for i in range(len(calificaciones)):
            if calificaciones[i] > mayor:
                mayor = calificaciones[i]
                pos_mayor = i
            if calificaciones[i] < menor:
                menor = calificaciones[i]
                pos_menor = i
        print(f"Calificación más alta: {mayor} ({nombres[pos_mayor]})")
        print(f"Calificación más baja: {menor} ({nombres[pos_menor]})")

    elif opcion == 5:
        aprobados = 0
        reprobados = 0
        for nota in calificaciones:
            if nota >= NOTA_MINIMA:
                aprobados = aprobados + 1
            else:
                reprobados = reprobados + 1
        print(f"Aprobados: {aprobados}")
        print(f"Reprobados: {reprobados}")

    elif opcion == 6:
        buscado = input("Nombre a buscar: ").strip().lower()
        encontrado = False
        for i in range(len(nombres)):
            if nombres[i].lower() == buscado:
                print(f"{nombres[i]} está en la posición {i + 1} (índice {i}) con nota {calificaciones[i]}")
                encontrado = True
        if not encontrado:
            print("No se encontró ningún estudiante con ese nombre.")

    elif opcion == 7:
        entrada = input(f"Número del estudiante a modificar (1 a {len(calificaciones)}): ")
        if entrada.isdigit() and 1 <= int(entrada) <= len(calificaciones):
            indice = int(entrada) - 1
            nueva = input(f"Nueva calificación para {nombres[indice]} (0-100): ")
            if nueva.isdigit() and 0 <= int(nueva) <= 100:
                anterior = calificaciones[indice]
                calificaciones[indice] = int(nueva)
                print(f"Cambio realizado: {anterior} -> {calificaciones[indice]}")
                print("Vector actualizado:", calificaciones)
            else:
                print("Calificación no válida: debe ser un entero entre 0 y 100.")
        else:
            print("Número fuera de rango: no existe ese estudiante.")

    elif opcion == 8:
        print("\nVector final:", calificaciones)
        print("Gracias por usar el sistema. ¡Hasta pronto!")

    else:
        print("Opción no válida. Intente de nuevo.")