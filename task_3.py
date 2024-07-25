import heapq
import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

cities = [
    "Kyiv", "Kharkiv", "Odesa", "Dnipro", "Lviv"
]

# Відстані між містами (приклад, додайте інші)
edges = [
    ("Kyiv", "Kharkiv", 477),
    ("Kyiv", "Odesa", 475),
    ("Kyiv", "Dnipro", 477),
    ("Kyiv", "Lviv", 540),
    ("Kharkiv", "Dnipro", 213),
    ("Kharkiv", "Odesa", 673),
    ("Odesa", "Dnipro", 446),
    ("Lviv", "Dnipro", 861),
]

# Координати міст на карті
positions = {
    "Kyiv": (30.5234, 50.4501),
    "Kharkiv": (36.2304, 49.9935),
    "Odesa": (30.7233, 46.4825),
    "Dnipro": (35.0462, 48.4647),
    "Lviv": (24.0297, 49.8397),
}

G = nx.Graph()

# Додайте всі міста як вузли графу
for city in cities:
    G.add_node(city)

# Додайте ребра до графу
for A, B, weight in edges:
    G.add_edge(A, B, weight=weight)

def dijkstra(start):
    distances = {}
    queue = [(0, start)]
    distances[start] = 0

    while queue:
        (size, node) = heapq.heappop(queue)
        for neighbor in G[node]:
            new_size = size + G[node][neighbor].get("weight", 1)
            if neighbor not in distances or new_size < distances[neighbor]:
                distances[neighbor] = new_size
                heapq.heappush(queue, (new_size, neighbor))
    return distances

if __name__ == "__main__":
    # Створюємо таблицю відстаней
    table = []

    for city in cities:
        distances_from_city = [dijkstra(city).get(other_city, float('inf')) for other_city in cities]
        table.append([f"{city} (0)"] + distances_from_city)

    headers = ["City"] + cities
    print(tabulate(table, headers=headers, tablefmt="pipe"))

    fig, ax = plt.subplots(figsize=(10, 10))

    # Відображення графа 
    nx.draw(G, positions, with_labels=True, node_size=500, node_color='yellow', font_size=10, edge_color='blue', ax=ax)

    # Додавання міток з відстанями
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels, ax=ax, font_color='black')

    plt.show()
