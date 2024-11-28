from process import process

def greedy_coloring(graph):
    # Initialize the result dictionary to store the color of each node
    result = {}

    # Assign the first color to the first node
    for node in graph:
        # Find the first available color
        available_colors = [True] * len(graph)
        for neighbor in graph[node]:
            if neighbor in result:
                color = result[neighbor]
                available_colors[color] = False

        # Assign the first available color
        for color, available in enumerate(available_colors):
            if available:
                result[node] = color
                break

    return result

def main():
    graph = process()
    result = greedy_coloring(graph)
    num_colors = len(set(result.values()))
    print(f"Minimum number of colors needed: {num_colors}")

if __name__ == "__main__":
    main()
