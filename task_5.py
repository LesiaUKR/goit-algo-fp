import heapq
import networkx as nx
import matplotlib.pyplot as plt
import uuid

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree_subplot(ax, tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    ax.set_title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, ax=ax, font_color='orange')

def build_tree_from_heap(arr):
    if not arr:
        return None

    # Інвертуємо значення для побудови мінімальної купи
    arr = [-i for i in arr]
    
    # Створюємо heap з масиву
    heapq.heapify(arr)
    
    # Інвертуємо значення назад для побудови максимального heap
    arr = [-i for i in arr]

    nodes = [Node(arr[i]) for i in range(len(arr))]
    for i in range(len(nodes) // 2):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0]

def bfs_visualization(root):
    if not root:
        return
    
    queue = [root]
    visited = []
    step = 32
    
    while queue:
        node = queue.pop(0)
        visited.append(node)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    # Присвоюємо кольори
    for i, node in enumerate(visited):
        intensity = hex(255 - i * step).split('x')[-1].zfill(2)
        node.color = f'#00{intensity}00'

def dfs_visualization(root):
    if not root:
        return
    
    stack = [root]
    visited = []
    step = 32
    
    while stack:
        node = stack.pop()
        visited.append(node)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    # Присвоюємо кольори
    for i, node in enumerate(visited):
        intensity = hex(255 - i * step).split('x')[-1].zfill(2)
        node.color = f'#00{intensity}00'

def main():
    arr = [10, 3, 8, 7, 6, 5, 4,1]
    root = build_tree_from_heap(arr)
    
    # Створюємо копію дерева для другого обходу
    root_bfs = build_tree_from_heap(arr)
    root_dfs = build_tree_from_heap(arr)
    
    bfs_visualization(root_bfs)
    dfs_visualization(root_dfs)
    
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))
    
    draw_tree_subplot(axs[0], root_bfs, "BFS Visualization")
    draw_tree_subplot(axs[1], root_dfs, "DFS Visualization")
    
    plt.show()

if __name__ == "__main__":
    main()
