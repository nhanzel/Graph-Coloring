import random
import os

def generate_graph(num_nodes, num_edges, output_file="data12.txt"):
    edges = set()
    
    # Generate edges until we reach the desired count
    while len(edges) < num_edges:
        v1 = random.randint(1, num_nodes)
        v2 = random.randint(1, num_nodes)
        if v1 != v2:
            edge = tuple(sorted((v1, v2)))  # Ensure no duplicate or self-loop
            edges.add(edge)
    
    # Write edges to the output file
    with open(output_file, "w") as file:
        for v1, v2 in edges:
            file.write(f"{v1} {v2}\n")
    
    print(f"Graph with {num_nodes} nodes and {num_edges} edges written to {output_file}")

# Run the function
generate_graph(100, 500)
