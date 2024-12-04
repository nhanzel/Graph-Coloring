import re

def process():
    # Read the data from the file
    with open('data12.txt', 'r') as file:
        lines = file.readlines()

    # Initialize an empty dictionary to store the graph
    graph = {}

    # Process each line and split into key and value
    for line in lines:
        key, value = re.split(r'[\t\s]+', line.strip())
        if key not in graph:
            graph[key] = []
        graph[key].append(value)
        if value not in graph:
            graph[value] = []
        graph[value].append(key)

    return graph