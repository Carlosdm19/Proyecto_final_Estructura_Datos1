# Definición de hechos (predicados)
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
