import tkinter as tk

class Rule:
    def __init__(self, premises, conclusion):
        self.premises = premises
        self.conclusion = conclusion

class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules

    def infer(self, query):
        for rule in self.rules:
            if all(premise in query for premise in rule.premises):
                query.add(rule.conclusion)
        return query

def create_inference_engine():
    rule1 = Rule({"A", "B"}, "C")
    rule2 = Rule({"D"}, "B")
    rule3 = Rule({"C"}, "E")

    rules = [rule1, rule2, rule3]
    engine = InferenceEngine(rules)
    return engine

def show_inference():
    engine = create_inference_engine()
    query = {"A", "D"}
    result = engine.infer(query)
    inference_label.configure(text=f"Inferencia: {result}")

# Crear ventana
window = tk.Tk()
window.title("Inferencia Lógica")
window.geometry("300x200")

# Crear etiqueta para mostrar la inferencia
inference_label = tk.Label(window, text="", font=("Arial", 12))
inference_label.pack(pady=10)

# Botón para mostrar la inferencia
infer_button = tk.Button(window, text="Realizar Inferencia", command=show_inference)
infer_button.pack(pady=10)

# Iniciar el bucle de la interfaz gráfica
window.mainloop()
