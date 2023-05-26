import tkinter as tk


base_de_datos = [
    
    ("Padre", "Juan", "Pedro"),
    ("Padre", "Juan", "María"),
    ("Padre", "Pedro", "Luis"),
    ("Madre", "María", "Luis"),
    
    
    ("Abuelo", "X", "Y", ["Padre", "X", "Z"], ["Padre", "Z", "Y"]),
    ("Abuela", "X", "Y", ["Madre", "X", "Z"], ["Madre", "Z", "Y"])
]


def consultar_base_de_datos(query):
    for elemento in base_de_datos:
        if elemento[0] == query[0] and elemento[1:] == query[1:]:
            return True
    return False


def realizar_consulta():
    consulta = (predicado_entry.get(), argumento1_entry.get(), argumento2_entry.get())
    resultado = consultar_base_de_datos(consulta)
    resultado_label.config(text=str(resultado))


root = tk.Tk()
root.title("Consulta de Base de datos")


predicado_label = tk.Label(root, text="Predicado:")
predicado_label.pack()
predicado_entry = tk.Entry(root)
predicado_entry.pack()


argumento1_label = tk.Label(root, text="Argumento 1:")
argumento1_label.pack()
argumento1_entry = tk.Entry(root)
argumento1_entry.pack()


argumento2_label = tk.Label(root, text="Argumento 2:")
argumento2_label.pack()
argumento2_entry = tk.Entry(root)
argumento2_entry.pack()


consulta_button = tk.Button(root, text="Consultar", command=realizar_consulta)
consulta_button.pack()


resultado_label = tk.Label(root, text="")
resultado_label.pack()


root.mainloop()

