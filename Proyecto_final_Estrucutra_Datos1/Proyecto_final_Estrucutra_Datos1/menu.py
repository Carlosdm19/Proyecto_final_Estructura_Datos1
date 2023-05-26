import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from problog.logic import Term
from problog.program import PrologString
from problog import get_evaluatable

def ejemplo_logica_primer_orden():
    
    # Declaración de constantes
    Constant('Juan')
    Constant('Maria')

    # Declaración de predicados
    Predicate('EsPadre', 2)
    Predicate('EsHijo', 2)
    Predicate('EsHermano', 2)

    # Reglas y hechos
    Rule(EsPadre(Juan, Maria))
    Rule(EsHijo(Maria, Juan))
    Rule(EsHermano(Juan, Maria))

    # Consultas
    print("Consulta 1:")
    print(ask(EsPadre(Juan, Maria)))

    print("Consulta 2:")
    print(ask(EsHermano(Juan, Maria)))

    print("Consulta 3:")
    print(ask(EsHijo(Maria, Juan)))
    messagebox.showinfo("Ejemplo de Lógica de Primer Orden", "Aquí iría el código del ejemplo de lógica de primer orden.")

def ejemplo_base_conocimiento():
    es_mamifero = {
    'perro',
    'gato',
    'elefante',
    'ballena'
}

es_ave = {
    'loro',
    'aguila',
    'pinguino'
}

es_reptil = {
    'cocodrilo',
    'serpiente',
    'lagarto'
}

es_anfibio = {
    'rana',
    'salamandra'
}

es_pez = {
    'atun',
    'trucha',
    'tiburon'
}

# Reglas lógicas
def es_animal(animal):
    return (
        animal in es_mamifero or
        animal in es_ave or
        animal in es_reptil or
        animal in es_anfibio or
        animal in es_pez
    )

def es_terrestre(animal):
    return (
        animal in es_mamifero or
        animal in es_reptil or
        animal in es_anfibio
    )

def es_volador(animal):
    return animal in es_ave

def es_acuatico(animal):
    return animal in es_pez

# Consultas a la base de conocimiento
animal = input("Ingresa el nombre de un animal: ")

if es_animal(animal):
    print(f"{animal} es un animal.")
    if es_terrestre(animal):
        print(f"{animal} es terrestre.")
    if es_volador(animal):
        print(f"{animal} es volador.")
    if es_acuatico(animal):
        print(f"{animal} es acuático.")
else:
    print(f"{animal} no se encuentra en la base de conocimiento.")
    messagebox.showinfo("Ejemplo de Base de Conocimiento", "Aquí iría el código del ejemplo de una base de conocimiento.")

def ejemplo_sistema_experto():
    # Sistema experto
    messagebox.showinfo("Ejemplo de Sistema Experto", "Aquí iría el código del ejemplo de un sistema experto.")

def ejemplo_procesamiento_lenguaje_natural():
    # Procesamiento de lenguaje natural
    messagebox.showinfo("Ejemplo de Procesamiento de Lenguaje Natural", "Aquí iría el código del ejemplo de procesamiento de lenguaje natural.")

def ejemplo_sistema_planificacion():
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
    messagebox.showinfo("Ejemplo de Sistema de Planificación", "Aquí iría el código del ejemplo de un sistema de planificación.")

def mostrar_menu():
    root = tk.Tk()
    root.title("Menú Principal")

    # Etiqueta de bienvenida
    etiqueta = tk.Label(root, text="Seleccione una opción:")
    etiqueta.pack(pady=10)

    # Botones de opciones
    boton1 = tk.Button(root, text="Lógica de Primer Orden", command=ejemplo_logica_primer_orden)
    boton1.pack(pady=5)

    boton2 = tk.Button(root, text="Base de Conocimiento", command=ejemplo_base_conocimiento)
    boton2.pack(pady=5)

    boton3 = tk.Button(root, text="Sistema Experto", command=ejemplo_sistema_experto)
    boton3.pack(pady=5)

    boton4 = tk.Button(root, text="Procesamiento de Lenguaje Natural", command=ejemplo_procesamiento_lenguaje_natural)
    boton4.pack(pady=5)

    boton5 = tk.Button(root, text="Sistema de Planificación", command=ejemplo_sistema_planificacion)
    boton5.pack(pady=5)

    root.mainloop()

# Mostrar el menú principal
mostrar_menu()

