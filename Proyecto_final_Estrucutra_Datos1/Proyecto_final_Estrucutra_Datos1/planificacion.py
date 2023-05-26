# Definición de acciones y precondiciones
acciones = {
    'accion_1': {
        'precondiciones': ['estado_a', 'estado_b'],
        'efectos': ['estado_c']
    },
    'accion_2': {
        'precondiciones': ['estado_c'],
        'efectos': ['estado_d']
    },
    'accion_3': {
        'precondiciones': ['estado_d'],
        'efectos': ['estado_e']
    },
    'accion_4': {
        'precondiciones': ['estado_e'],
        'efectos': ['estado_f']
    }
}

# Función de planificación
def planificar(estado_inicial, estado_final):
    plan = []
    estado_actual = estado_inicial

    while estado_actual != estado_final:
        accion_encontrada = False

        for accion, detalles in acciones.items():
            precondiciones = detalles['precondiciones']
            efectos = detalles['efectos']

            if all(condicion in estado_actual for condicion in precondiciones) and any(efecto not in estado_actual for efecto in efectos):
                plan.append(accion)
                estado_actual += [efecto for efecto in efectos if efecto not in estado_actual]
                accion_encontrada = True
                break

        if not accion_encontrada:
            print("No se encontró un plan válido.")
            return None

    return plan

# Ejemplo de planificación
estado_inicial = ['estado_a']
estado_final = ['estado_f']

plan_resultante = planificar(estado_inicial, estado_final)

if plan_resultante:
    print("Plan encontrado:")
    for i, accion in enumerate(plan_resultante, start=1):
        print(f"{'Paso ' + str(i)}: {accion}")
