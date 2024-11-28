from process import process

def is_valid_coloring(node, color, coloring, graph):
    for neighbor in graph[node]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def backtracking_coloring(graph, node, coloring, num_colors):
    if len(coloring) == len(graph):
        return coloring

    for color in range(num_colors):
        if is_valid_coloring(node, color, coloring, graph):
            coloring[node] = color
            next_node = next((n for n in graph if n not in coloring), None)
            if next_node is None:
                return coloring
            result = backtracking_coloring(graph, next_node, coloring, num_colors)
            if result:
                return result
            del coloring[node]

    return None

def find_min_colors(graph):
    num_colors = 1
    while True:
        coloring = backtracking_coloring(graph, next(iter(graph)), {}, num_colors)
        if coloring:
            return coloring, num_colors
        num_colors += 1

def main():
    graph = process()
    coloring, num_colors = find_min_colors(graph)
    print(f"Minimum number of colors needed: {num_colors}")

if __name__ == "__main__":
    main()
