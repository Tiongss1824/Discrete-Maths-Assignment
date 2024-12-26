import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# Define a simple scale (C major scale for simplicity)
notes = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88,
}

# Define a simple graph for transitions
graph = {
    "C": ["D", "E", "G"],
    "D": ["E", "F", "A"],
    "E": ["F", "G", "B"],
    "F": ["G", "A", "C"],
    "G": ["A", "B", "D"],
    "A": ["B", "C", "D"],
    "B": ["C", "D", "E"],
}

# Function to generate a random melody based on transitions
def generate_melody(start_note, length=50):
    melody = [start_note]
    current_note = start_note
    for _ in range(length - 1):
        next_note = random.choice(graph[current_note])
        melody.append(next_note)
        current_note = next_note
    return melody

# Generate the melody
melody = generate_melody("C", 50)

# Count the transitions between notes
transitions = [(melody[i], melody[i+1]) for i in range(len(melody)-1)]
transition_counts = Counter(transitions)

# Create a graph to store transitions
G = nx.DiGraph()

# Add edges to the graph with transition counts as weights
for (note_from, note_to), count in transition_counts.items():
    G.add_edge(note_from, note_to, weight=count)

# Draw the graph with labels showing the transition weights
pos = nx.spring_layout(G, seed=42)  # Positioning of nodes
plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=15, font_weight='bold', edge_color='gray', width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
plt.title("Transitions Between Notes in a Melody (Anime BGM Inspired)")
plt.show()
