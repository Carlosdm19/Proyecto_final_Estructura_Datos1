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
