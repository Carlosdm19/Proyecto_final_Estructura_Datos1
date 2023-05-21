import tkinter as tk
from anytree import Node, RenderTree

def create_tree():
    root = Node('∨')
    and_node = Node('∧', parent=root)
    p_node = Node('P', parent=and_node)
    q_node = Node('Q', parent=and_node)
    r_node = Node('R', parent=root)
    return root

def show_tree():
    root_node = create_tree()
    tree_str = ""
    for pre, _, node in RenderTree(root_node):
        tree_str += f"{pre}{node.name}\n"
    tree_label.configure(text=tree_str)


window = tk.Tk()
window.title("Árbol Sintáctico")
window.geometry("300x200")


tree_label = tk.Label(window, text="", font=("Arial", 12))
tree_label.pack(pady=10)


show_button = tk.Button(window, text="Mostrar Árbol", command=show_tree)
show_button.pack(pady=10)


window.mainloop()
