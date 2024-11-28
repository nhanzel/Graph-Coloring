from process import process

def dsatur_coloring(graph):
    # Initialize the result dictionary to store the color of each node
    result = {}
    # Initialize the saturation degree and degree of each node
    saturation_degree = {node: 0 for node in graph}
    degree = {node: len(neighbors) for node, neighbors in graph.items()}

    # Assign the first color to the node with the highest degree
    start_node = max(degree, key=degree.get)
    result[start_node] = 0

    # Update the saturation degree of the neighbors
    for neighbor in graph[start_node]:
        saturation_degree[neighbor] += 1

    while len(result) < len(graph):
        # Select the next node with the highest saturation degree
        # Break ties by selecting the node with the highest degree
        next_node = max(
            (node for node in graph if node not in result),
            key=lambda node: (saturation_degree[node], degree[node])
        )

        # Find the first available color
        available_colors = [True] * len(graph)
        for neighbor in graph[next_node]:
            if neighbor in result:
                color = result[neighbor]
                available_colors[color] = False

        # Assign the first available color
        for color, available in enumerate(available_colors):
            if available:
                result[next_node] = color
                break

        # Update the saturation degree of the neighbors
        for neighbor in graph[next_node]:
            if neighbor not in result:
                saturation_degree[neighbor] += 1

    return result

def main():
    graph = process()
    result = dsatur_coloring(graph)
    num_colors = len(set(result.values()))
    print(f"Minimum number of colors needed: {num_colors}")

if __name__ == "__main__":
    main()
