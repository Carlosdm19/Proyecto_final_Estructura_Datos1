import tkinter as tk

class Variable:
    def __init__(self, name):
        self.name = name

class Function:
    def __init__(self, name, args):
        self.name = name
        self.args = args

def unify_variable(variable, term, substitution):
    if variable.name in substitution:
        return unify(substitution[variable.name], term, substitution)
    elif isinstance(term, Variable) and term.name in substitution:
        return unify(variable, substitution[term.name], substitution)
    else:
        substitution[variable.name] = term
        return substitution

def unify(term1, term2, substitution):
    if term1 == term2:
        return substitution
    elif isinstance(term1, Variable):
        return unify_variable(term1, term2, substitution)
    elif isinstance(term2, Variable):
        return unify_variable(term2, term1, substitution)
    elif isinstance(term1, Function) and isinstance(term2, Function):
        if term1.name == term2.name and len(term1.args) == len(term2.args):
            for arg1, arg2 in zip(term1.args, term2.args):
                substitution = unify(arg1, arg2, substitution)
            return substitution
        else:
            return None
    else:
        return None

def create_terms():
    term1 = Function('f', ['a', Variable('X')])
    term2 = Function('f', [Variable('Y'), Variable('b')])
    substitution = unify(term1, term2, {})
    return substitution

def show_unification():
    substitution = create_terms()
    if substitution is not None:
        unification_str = ""
        for var, value in substitution.items():
            unification_str += f"{var} = {value}\n"
        unification_label.configure(text=unification_str)
    else:
        unification_label.configure(text="No se puede unificar")

# Crear ventana
window = tk.Tk()
window.title("Unificación")
window.geometry("300x200")

# Crear etiqueta para mostrar la unificación
unification_label = tk.Label(window, text="", font=("Arial", 12))
unification_label.pack(pady=10)

# Botón para mostrar la unificación
show_button = tk.Button(window, text="Mostrar Unificación", command=show_unification)
show_button.pack(pady=10)

# Iniciar el bucle de la interfaz gráfica
window.mainloop()

window.title("Unificación")
window.geometry("300x200")

# Crear etiqueta para mostrar la unificación
unification_label = tk.Label(window, text="", font=("Arial", 12))
unification_label.pack(pady=10)

# Botón para mostrar la unificación
show_button = tk.Button(window, text="Mostrar Unificación", command=show_unification)
show_button.pack(pady=10)

# Iniciar el bucle de la interfaz gráfica
window.mainloop()


