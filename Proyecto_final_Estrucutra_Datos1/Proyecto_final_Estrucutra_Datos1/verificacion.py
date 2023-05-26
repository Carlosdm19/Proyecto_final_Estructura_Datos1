from z3 import *

def verificar_ascendencia(numeros):
    solver = Solver()

    # Variables
    variables = [Int(f"num_{i}") for i in range(len(numeros))]

    # Restricciones
    restricciones = []
    for i in range(len(numeros) - 1):
        restricciones.append(variables[i] < variables[i+1])

    # Añadir restricciones al solver
    solver.add(restricciones)

    # Verificar si es satisfacible
    if solver.check() == sat:
        modelo = solver.model()
        numeros_ascendentes = [modelo[variables[i]].as_long() for i in range(len(numeros))]
        return numeros_ascendentes
    else:
        return None

# Ejemplo de verificación
numeros = [1, 2, 3, 4, 5]
resultado = verificar_ascendencia(numeros)

if resultado:
    print(f"Los números {numeros} son ascendentes.")
    print(f"Números ascendentes: {resultado}")
else:
    print(f"Los números {numeros} no son ascendentes.")
