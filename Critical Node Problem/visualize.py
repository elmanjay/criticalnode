import os
import ast
import networkx as nx
import matplotlib.pyplot as plt

# Datei öffnen und Zeilen lesen
with open('raw/rndgraph05-20_1-1-1_001.txt', 'r') as file:
    lines = file.readlines()

# Initialisierung der Variablen
V = []
A = []

# Durch die Zeilen iterieren und Werte extrahieren
for line in lines:
    line = line.strip()
    if line.startswith("V ="):
        V = ast.literal_eval(line.split('=', 1)[1].strip())
    elif line.startswith("A ="):
        A = ast.literal_eval(line.split('=', 1)[1].strip())

G = nx.DiGraph()

# Knoten und Kanten hinzufügen
G.add_nodes_from(V)
G.add_edges_from(A)

# Netzwerk visualisieren
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Layout für die Knotenpositionen
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10, arrows=True)
plt.title("Visualisierung des gerichteten Netzwerks")
plt.show()