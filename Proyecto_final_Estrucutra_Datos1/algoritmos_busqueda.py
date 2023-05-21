import tkinter as tk
from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def create_tree():
    
    root = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')
    node_e = Node('E')
    node_f = Node('F')

    root.children = [node_b, node_c]
    node_b.children = [node_d, node_e]
    node_c.children = [node_f]

    return root

def dfs(root, search_value):
    stack = [root]
    visited = set()

    while stack:
        current_node = stack.pop()

        if current_node.value == search_value:
            return True

        visited.add(current_node)

        for child in current_node.children:
            if child not in visited:
                stack.append(child)

    return False

def bfs(root, search_value):
    queue = Queue()
    queue.put(root)
    visited = set()

    while not queue.empty():
        current_node = queue.get()

        if current_node.value == search_value:
            return True

        visited.add(current_node)

        for child in current_node.children:
            if child not in visited:
                queue.put(child)

    return False

def perform_dfs():
    search_value = search_entry.get()
    result = dfs(tree, search_value)
    if result:
        result_label.configure(text=f"{search_value} encontrado (DFS)")
    else:
        result_label.configure(text=f"{search_value} no encontrado (DFS)")

def perform_bfs():
    search_value = search_entry.get()
    result = bfs(tree, search_value)
    if result:
        result_label.configure(text=f"{search_value} encontrado (BFS)")
    else:
        result_label.configure(text=f"{search_value} no encontrado (BFS)")


window = tk.Tk()
window.title("Algoritmos de Búsqueda")
window.geometry("300x200")

tree = create_tree()


search_entry = tk.Entry(window)
search_entry.pack(pady=10)


dfs_button = tk.Button(window, text="Búsqueda en Profundidad (DFS)", command=perform_dfs)
dfs_button.pack(pady=5)


bfs_button = tk.Button(window, text="Búsqueda en Anchura (BFS)", command=perform_bfs)
bfs_button.pack(pady=5)


result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)


window.mainloop()
