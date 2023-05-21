import tkinter as tk

class Predicate:
    def __init__(self, name, args):
        self.name = name
        self.args = args

class Function:
    def __init__(self, name, args):
        self.name = name
        self.args = args

def create_formula():
    predicate = Predicate('P', ['x', 'y'])
    return predicate

def show_formula():
    formula = create_formula()
    formula_str = f"{formula.name}({', '.join(formula.args)})"
    formula_label.configure(text=formula_str)


window = tk.Tk()
window.title("Representación de Fórmulas")
window.geometry("300x200")


formula_label = tk.Label(window, text="", font=("Arial", 12))
formula_label.pack(pady=10)


show_button = tk.Button(window, text="Mostrar Fórmula", command=show_formula)
show_button.pack(pady=10)


window.mainloop()
