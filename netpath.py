# Simple graph theory to check for network isolation and survivability scenarios
# Great tip on switching from functions to a graph class from Berd Klein at Bodenseo

# This is the function approach

# Decision...Do we consider Network Carriers to be nodes?
# For example, is Time Warner providing connections in a data center itself a node?

graph = {"HQ": ["DC1", "DC2"],
         "BackOffice": ["DC1", "DC2"],
         "DC1": ["HQ", "BackOffice", "DC2", "Colo1", "Colo2", "Colo3"],
         "DC2": ["HQ", "BackOffice", "DC1", "Colo1", "Colo2", "Colo3"],
         "Colo1": ["DC2", "Colo3"],
         "Colo2": ["DC1"],
         "Colo3": ["Colo1"],
         "Colo4": []
         }

print('Starting graph analysis')
print('This is printing the old way')


def generate_edge(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))
    return edges


def isolated_node_check(graph):
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated


print('\nGenerating node graph: \n', generate_edge(graph), '\n')

print('\nChecking for isolated nodes: \n', isolated_node_check(graph), '\n')
