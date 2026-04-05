def calcular_puntajes(ronda):
    puntajes_ronda = {}

    for cocinero, jueces in ronda['scores'].items():
        total = sum(jueces.values())
        puntajes_ronda[cocinero] = total

    return puntajes_ronda


def actualizar_tabla(tabla, puntajes_ronda):
    for cocinero, puntos in puntajes_ronda.items():
        tabla[cocinero]["total"] += puntos

        if puntos > tabla[cocinero]["mejor"]:
            tabla[cocinero]["mejor"] = puntos


def mostrar_tabla(tabla):
    ordenados = sorted(tabla.items(), key=lambda x: x[1]["total"], reverse=True)

    print("Tabla de posiciones (acumulada):")
    for nombre, datos in ordenados:
        print(f"{nombre}: {datos['total']} pts | Ganadas: {datos['ganadas']} | Mejor: {datos['mejor']}")


def mostrar_tabla_final(tabla, rounds):
    ordenados = sorted(tabla.items(), key=lambda x: x[1]["total"], reverse=True)

    print("\nTabla de posiciones final:")
    print(f"{'Cocinero':<14}{'Puntaje':<10}{'Ganadas':<10}{'Mejor':<10}{'Promedio':<10}")
    print("-"*55)

    for nombre, datos in ordenados:
        promedio = datos["total"] / len(rounds)
        print(f"{nombre:<14}{datos['total']:<10}{datos['ganadas']:<10}{datos['mejor']:<10}{promedio:.1f}")